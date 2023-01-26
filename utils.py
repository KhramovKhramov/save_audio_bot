from clarifai_grpc.channel.clarifai_channel import ClarifaiChannel
from clarifai_grpc.grpc.api import resources_pb2, service_pb2, service_pb2_grpc
from clarifai_grpc.grpc.api.status import status_code_pb2
import settings
from pydub import AudioSegment
from pydub.utils import mediainfo
import os

def has_oblect_on_image(file_name, object_name):
    channel = ClarifaiChannel.get_grpc_channel()
    app = service_pb2_grpc.V2Stub(channel)
    metadata = (('authorization', f'Key {settings.CLARIFAI_API_KEY}'),)

    with open(file_name, 'rb') as f:
        file_data = f.read()
        image = resources_pb2.Image(base64=file_data)

    request = service_pb2.PostModelOutputsRequest(
        model_id='aaa03c23b3724a16a56b629203edc62c',
        inputs=[
            resources_pb2.Input(data=resources_pb2.Data(image=image))
        ])

    response = app.PostModelOutputs(request, metadata=metadata)
    return check_responce_for_object(response, object_name=object_name)


def check_responce_for_object(response, object_name):
    if response.status.code == status_code_pb2.SUCCESS:
        for concept in response.outputs[0].data.concepts:
            if concept.name == object_name and concept.value >= 0.8:
                return True
    else:
        print(f"Ошибка распознавания: {response.outputs[0].status.details}")

    return False

def export_to_wav(file_name, user_id, file_id, format):
    sound = AudioSegment.from_file(file_name, format)
    os.makedirs(f'files/user_{user_id}/audio', exist_ok=True)
    output_filename = os.path.join(f'files/user_{user_id}/audio', f'{file_id}.wav')
    sound.export(output_filename, format='wav', bitrate='320к')
