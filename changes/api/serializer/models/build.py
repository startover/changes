from changes.api.serializer import Serializer, register
from changes.models import Build


@register(Build)
class BuildSerializer(Serializer):
    def serialize(self, instance):
        if instance.project_id:
            avg_build_time = instance.project.avg_build_time
        else:
            avg_build_time = None

        target = instance.target
        if target is None and instance.revision_sha:
            target = instance.revision_sha[:12]

        if instance.revision_sha:
            revision = {
                'sha': instance.revision_sha,
            }
        else:
            revision = None

        if instance.patch_id:
            patch = {
                'id': instance.patch_id.hex,
            }
        else:
            patch = None

        return {
            'id': instance.id.hex,
            'number': instance.number,
            'name': instance.label,
            'target': target,
            'result': instance.result,
            'status': instance.status,
            'project': instance.project,
            'cause': instance.cause,
            'author': instance.author,
            'source': {
                'revision': revision,
                'patch': patch,
            },
            'message': instance.message,
            'duration': instance.duration,
            'estimatedDuration': avg_build_time,
            'link': '/builds/%s/' % (instance.id.hex,),
            'dateCreated': instance.date_created.isoformat(),
            'dateModified': instance.date_modified.isoformat() if instance.date_modified else None,
            'dateStarted': instance.date_started.isoformat() if instance.date_started else None,
            'dateFinished': instance.date_finished.isoformat() if instance.date_finished else None,
        }