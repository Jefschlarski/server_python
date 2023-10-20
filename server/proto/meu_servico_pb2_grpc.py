# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

import server.proto.meu_servico_pb2 as meu__servico__pb2


class MeuServicoStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.MeuMetodo = channel.unary_unary(
                '/meu_servico.MeuServico/MeuMetodo',
                request_serializer=meu__servico__pb2.MinhaRequisicao.SerializeToString,
                response_deserializer=meu__servico__pb2.MinhaResposta.FromString,
                )
        self.MetodoOrdemServico = channel.unary_unary(
                '/meu_servico.MeuServico/MetodoOrdemServico',
                request_serializer=meu__servico__pb2.OrdemServicoRequisicao.SerializeToString,
                response_deserializer=meu__servico__pb2.OrdemServicoList.FromString,
                )
        self.getImage = channel.unary_unary(
                '/meu_servico.MeuServico/getImage',
                request_serializer=meu__servico__pb2.Imagem.SerializeToString,
                response_deserializer=meu__servico__pb2.Resposta.FromString,
                )


class MeuServicoServicer(object):
    """Missing associated documentation comment in .proto file."""

    def MeuMetodo(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def MetodoOrdemServico(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def getImage(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_MeuServicoServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'MeuMetodo': grpc.unary_unary_rpc_method_handler(
                    servicer.MeuMetodo,
                    request_deserializer=meu__servico__pb2.MinhaRequisicao.FromString,
                    response_serializer=meu__servico__pb2.MinhaResposta.SerializeToString,
            ),
            'MetodoOrdemServico': grpc.unary_unary_rpc_method_handler(
                    servicer.MetodoOrdemServico,
                    request_deserializer=meu__servico__pb2.OrdemServicoRequisicao.FromString,
                    response_serializer=meu__servico__pb2.OrdemServicoList.SerializeToString,
            ),
            'getImage': grpc.unary_unary_rpc_method_handler(
                    servicer.getImage,
                    request_deserializer=meu__servico__pb2.Imagem.FromString,
                    response_serializer=meu__servico__pb2.Resposta.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'meu_servico.MeuServico', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class MeuServico(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def MeuMetodo(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/meu_servico.MeuServico/MeuMetodo',
            meu__servico__pb2.MinhaRequisicao.SerializeToString,
            meu__servico__pb2.MinhaResposta.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def MetodoOrdemServico(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/meu_servico.MeuServico/MetodoOrdemServico',
            meu__servico__pb2.OrdemServicoRequisicao.SerializeToString,
            meu__servico__pb2.OrdemServicoList.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def getImage(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/meu_servico.MeuServico/getImage',
            meu__servico__pb2.Imagem.SerializeToString,
            meu__servico__pb2.Resposta.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)