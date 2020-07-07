## GrpcNativeLibsCopier

This is an example .csproj file that copies Grpc native libraries (windows only)
to set of target directories.

Intended to be used with Grpc_SkipNativeLibsCopy = true msbuild flag.

See also:

- https://github.com/grpc/grpc/issues/21867
- https://github.com/grpc/grpc/pull/22894

This is using Paket and is not buildable alone. Should be adapted for your real build environment.
