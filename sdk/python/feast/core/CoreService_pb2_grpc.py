# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
import grpc

from feast.core import CoreService_pb2 as feast_dot_core_dot_CoreService__pb2
from feast.specs import EntitySpec_pb2 as feast_dot_specs_dot_EntitySpec__pb2
from feast.specs import FeatureGroupSpec_pb2 as feast_dot_specs_dot_FeatureGroupSpec__pb2
from feast.specs import FeatureSpec_pb2 as feast_dot_specs_dot_FeatureSpec__pb2
from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2


class CoreServiceStub(object):
  # missing associated documentation comment in .proto file
  pass

  def __init__(self, channel):
    """Constructor.

    Args:
      channel: A grpc.Channel.
    """
    self.GetEntities = channel.unary_unary(
        '/feast.core.CoreService/GetEntities',
        request_serializer=feast_dot_core_dot_CoreService__pb2.CoreServiceTypes.GetEntitiesRequest.SerializeToString,
        response_deserializer=feast_dot_core_dot_CoreService__pb2.CoreServiceTypes.GetEntitiesResponse.FromString,
        )
    self.ListEntities = channel.unary_unary(
        '/feast.core.CoreService/ListEntities',
        request_serializer=google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
        response_deserializer=feast_dot_core_dot_CoreService__pb2.CoreServiceTypes.ListEntitiesResponse.FromString,
        )
    self.GetStorage = channel.unary_unary(
        '/feast.core.CoreService/GetStorage',
        request_serializer=feast_dot_core_dot_CoreService__pb2.CoreServiceTypes.GetStorageRequest.SerializeToString,
        response_deserializer=feast_dot_core_dot_CoreService__pb2.CoreServiceTypes.GetStorageResponse.FromString,
        )
    self.ListStorage = channel.unary_unary(
        '/feast.core.CoreService/ListStorage',
        request_serializer=google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
        response_deserializer=feast_dot_core_dot_CoreService__pb2.CoreServiceTypes.ListStorageResponse.FromString,
        )
    self.GetFeatures = channel.unary_unary(
        '/feast.core.CoreService/GetFeatures',
        request_serializer=feast_dot_core_dot_CoreService__pb2.CoreServiceTypes.GetFeaturesRequest.SerializeToString,
        response_deserializer=feast_dot_core_dot_CoreService__pb2.CoreServiceTypes.GetFeaturesResponse.FromString,
        )
    self.ListFeatures = channel.unary_unary(
        '/feast.core.CoreService/ListFeatures',
        request_serializer=google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
        response_deserializer=feast_dot_core_dot_CoreService__pb2.CoreServiceTypes.ListFeaturesResponse.FromString,
        )
    self.ApplyFeature = channel.unary_unary(
        '/feast.core.CoreService/ApplyFeature',
        request_serializer=feast_dot_specs_dot_FeatureSpec__pb2.FeatureSpec.SerializeToString,
        response_deserializer=feast_dot_core_dot_CoreService__pb2.CoreServiceTypes.ApplyFeatureResponse.FromString,
        )
    self.ApplyFeatureGroup = channel.unary_unary(
        '/feast.core.CoreService/ApplyFeatureGroup',
        request_serializer=feast_dot_specs_dot_FeatureGroupSpec__pb2.FeatureGroupSpec.SerializeToString,
        response_deserializer=feast_dot_core_dot_CoreService__pb2.CoreServiceTypes.ApplyFeatureGroupResponse.FromString,
        )
    self.ApplyEntity = channel.unary_unary(
        '/feast.core.CoreService/ApplyEntity',
        request_serializer=feast_dot_specs_dot_EntitySpec__pb2.EntitySpec.SerializeToString,
        response_deserializer=feast_dot_core_dot_CoreService__pb2.CoreServiceTypes.ApplyEntityResponse.FromString,
        )
    self.GetUploadUrl = channel.unary_unary(
        '/feast.core.CoreService/GetUploadUrl',
        request_serializer=feast_dot_core_dot_CoreService__pb2.CoreServiceTypes.GetUploadUrlRequest.SerializeToString,
        response_deserializer=feast_dot_core_dot_CoreService__pb2.CoreServiceTypes.GetUploadUrlResponse.FromString,
        )


class CoreServiceServicer(object):
  # missing associated documentation comment in .proto file
  pass

  def GetEntities(self, request, context):
    """
    Get entities specified in request.
    This process returns a list of entity specs.
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def ListEntities(self, request, context):
    """
    Get all entities
    This process returns a list of entity specs.
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def GetStorage(self, request, context):
    """
    Get storage specs specified in request.
    This process returns a list of storage specs.
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def ListStorage(self, request, context):
    """
    Get all storage specs.
    This process returns a list of storage specs.
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def GetFeatures(self, request, context):
    """
    Get features specified in request.
    This process returns a list of feature specs.
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def ListFeatures(self, request, context):
    """
    Get all features.
    This process returns a list of entity specs.
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def ApplyFeature(self, request, context):
    """
    Register a new feature to the metadata store, or update an existing feature.
    If any validation errors occur, only the first encountered error will be returned.
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def ApplyFeatureGroup(self, request, context):
    """
    Register a new feature group to the metadata store, or update an existing feature group.
    If any validation errors occur, only the first encountered error will be returned.
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def ApplyEntity(self, request, context):
    """
    Register a new entity to the metadata store, or update an existing entity.
    If any validation errors occur, only the first encountered error will be returned.
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def GetUploadUrl(self, request, context):
    """
    Request a signed URL where a Feast client can upload a feature values file for an import job.
    The signed URL be default will be valid by default for 5 minutes during which the client can start
    uploading the feature values file. As of 2019-06-28, only CSV and JSON files are supported,
    and the upload must complete in one PUT request i.e. resumable upload is not supported.
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')


def add_CoreServiceServicer_to_server(servicer, server):
  rpc_method_handlers = {
      'GetEntities': grpc.unary_unary_rpc_method_handler(
          servicer.GetEntities,
          request_deserializer=feast_dot_core_dot_CoreService__pb2.CoreServiceTypes.GetEntitiesRequest.FromString,
          response_serializer=feast_dot_core_dot_CoreService__pb2.CoreServiceTypes.GetEntitiesResponse.SerializeToString,
      ),
      'ListEntities': grpc.unary_unary_rpc_method_handler(
          servicer.ListEntities,
          request_deserializer=google_dot_protobuf_dot_empty__pb2.Empty.FromString,
          response_serializer=feast_dot_core_dot_CoreService__pb2.CoreServiceTypes.ListEntitiesResponse.SerializeToString,
      ),
      'GetStorage': grpc.unary_unary_rpc_method_handler(
          servicer.GetStorage,
          request_deserializer=feast_dot_core_dot_CoreService__pb2.CoreServiceTypes.GetStorageRequest.FromString,
          response_serializer=feast_dot_core_dot_CoreService__pb2.CoreServiceTypes.GetStorageResponse.SerializeToString,
      ),
      'ListStorage': grpc.unary_unary_rpc_method_handler(
          servicer.ListStorage,
          request_deserializer=google_dot_protobuf_dot_empty__pb2.Empty.FromString,
          response_serializer=feast_dot_core_dot_CoreService__pb2.CoreServiceTypes.ListStorageResponse.SerializeToString,
      ),
      'GetFeatures': grpc.unary_unary_rpc_method_handler(
          servicer.GetFeatures,
          request_deserializer=feast_dot_core_dot_CoreService__pb2.CoreServiceTypes.GetFeaturesRequest.FromString,
          response_serializer=feast_dot_core_dot_CoreService__pb2.CoreServiceTypes.GetFeaturesResponse.SerializeToString,
      ),
      'ListFeatures': grpc.unary_unary_rpc_method_handler(
          servicer.ListFeatures,
          request_deserializer=google_dot_protobuf_dot_empty__pb2.Empty.FromString,
          response_serializer=feast_dot_core_dot_CoreService__pb2.CoreServiceTypes.ListFeaturesResponse.SerializeToString,
      ),
      'ApplyFeature': grpc.unary_unary_rpc_method_handler(
          servicer.ApplyFeature,
          request_deserializer=feast_dot_specs_dot_FeatureSpec__pb2.FeatureSpec.FromString,
          response_serializer=feast_dot_core_dot_CoreService__pb2.CoreServiceTypes.ApplyFeatureResponse.SerializeToString,
      ),
      'ApplyFeatureGroup': grpc.unary_unary_rpc_method_handler(
          servicer.ApplyFeatureGroup,
          request_deserializer=feast_dot_specs_dot_FeatureGroupSpec__pb2.FeatureGroupSpec.FromString,
          response_serializer=feast_dot_core_dot_CoreService__pb2.CoreServiceTypes.ApplyFeatureGroupResponse.SerializeToString,
      ),
      'ApplyEntity': grpc.unary_unary_rpc_method_handler(
          servicer.ApplyEntity,
          request_deserializer=feast_dot_specs_dot_EntitySpec__pb2.EntitySpec.FromString,
          response_serializer=feast_dot_core_dot_CoreService__pb2.CoreServiceTypes.ApplyEntityResponse.SerializeToString,
      ),
      'GetUploadUrl': grpc.unary_unary_rpc_method_handler(
          servicer.GetUploadUrl,
          request_deserializer=feast_dot_core_dot_CoreService__pb2.CoreServiceTypes.GetUploadUrlRequest.FromString,
          response_serializer=feast_dot_core_dot_CoreService__pb2.CoreServiceTypes.GetUploadUrlResponse.SerializeToString,
      ),
  }
  generic_handler = grpc.method_handlers_generic_handler(
      'feast.core.CoreService', rpc_method_handlers)
  server.add_generic_rpc_handlers((generic_handler,))
