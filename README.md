## GrpcNativeLibsCopier

This is an example .csproj file that copies Grpc native libraries (windows only)
to set of target directories.

Intended to be used with Grpc_SkipNativeLibsCopy = true msbuild flag.

See also:

- https://github.com/grpc/grpc/issues/21867
- https://github.com/grpc/grpc/pull/22894

This is using Paket and is not buildable alone. Should be adapted for your real build environment.


## Usage

Modify your problematic csproj file, or your global [Directory.Build.props](https://docs.microsoft.com/en-us/visualstudio/msbuild/customize-your-build?view=vs-2019#directorybuildprops-and-directorybuildtargets) file if you have one, by adding the following rule:

```xml
  <PropertyGroup>
      <Grpc_SkipNativeLibsCopy>true</Grpc_SkipNativeLibsCopy>
  </PropertyGroup>
```

This will prevent Grpc.Core nuget package from trying to copy the file on it's own (because it can fail and kill your whole build).

Then, just run 
```
msbuild GrpcNativeLibsCopier.csproj
```
somewhere in your build to actually copy your files.

Note that you need to add the wanted <OutPath> entries describing the target directories to the csproj files yourself. There is no automatic discovery whatsoever.
