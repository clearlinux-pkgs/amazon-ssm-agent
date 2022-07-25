#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : amazon-ssm-agent
Version  : 3.1.1575.0
Release  : 34
URL      : https://github.com/aws/amazon-ssm-agent/archive/3.1.1575.0/amazon-ssm-agent-3.1.1575.0.tar.gz
Source0  : https://github.com/aws/amazon-ssm-agent/archive/3.1.1575.0/amazon-ssm-agent-3.1.1575.0.tar.gz
Summary  : Manage EC2 Instances using SSM APIs
Group    : Development/Tools
License  : Apache-2.0 BSD-2-Clause BSD-3-Clause CC-BY-3.0 ISC MIT
Requires: amazon-ssm-agent-autostart = %{version}-%{release}
Requires: amazon-ssm-agent-bin = %{version}-%{release}
Requires: amazon-ssm-agent-data = %{version}-%{release}
Requires: amazon-ssm-agent-license = %{version}-%{release}
Requires: amazon-ssm-agent-services = %{version}-%{release}
BuildRequires : buildreq-golang
Patch1: 0001-Stateless-patch.patch

%description
This package provides Amazon SSM Agent for managing EC2 Instances using SSM APIs

%package autostart
Summary: autostart components for the amazon-ssm-agent package.
Group: Default

%description autostart
autostart components for the amazon-ssm-agent package.


%package bin
Summary: bin components for the amazon-ssm-agent package.
Group: Binaries
Requires: amazon-ssm-agent-data = %{version}-%{release}
Requires: amazon-ssm-agent-license = %{version}-%{release}
Requires: amazon-ssm-agent-services = %{version}-%{release}

%description bin
bin components for the amazon-ssm-agent package.


%package data
Summary: data components for the amazon-ssm-agent package.
Group: Data

%description data
data components for the amazon-ssm-agent package.


%package license
Summary: license components for the amazon-ssm-agent package.
Group: Default

%description license
license components for the amazon-ssm-agent package.


%package services
Summary: services components for the amazon-ssm-agent package.
Group: Systemd services

%description services
services components for the amazon-ssm-agent package.


%prep
%setup -q -n amazon-ssm-agent-3.1.1575.0
cd %{_builddir}/amazon-ssm-agent-3.1.1575.0
%patch1 -p1

%build
## build_prepend content
export GOFLAGS='-buildmode=pie' GO111MODULE="auto"
## build_prepend end
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1658769407
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=auto "
export FCFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=auto "
export FFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=auto "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=auto "
make  %{?_smp_mflags}  build-linux


%install
export SOURCE_DATE_EPOCH=1658769407
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/amazon-ssm-agent
cp %{_builddir}/amazon-ssm-agent-%{version}/LICENSE %{buildroot}/usr/share/package-licenses/amazon-ssm-agent/2b8b815229aa8a61e483fb4ba0588b8b6c491890
cp %{_builddir}/amazon-ssm-agent-%{version}/Tools/src/LICENSE %{buildroot}/usr/share/package-licenses/amazon-ssm-agent/b4f43f12b5c4f6bbaf183777fc64e38efb3e9aa5
cp %{_builddir}/amazon-ssm-agent-%{version}/extra/aws-sdk-go/LICENSE.txt %{buildroot}/usr/share/package-licenses/amazon-ssm-agent/2b8b815229aa8a61e483fb4ba0588b8b6c491890
cp %{_builddir}/amazon-ssm-agent-%{version}/extra/aws-sdk-go/internal/sync/singleflight/LICENSE %{buildroot}/usr/share/package-licenses/amazon-ssm-agent/d6a5f1ecaedd723c325a2063375b3517e808a2b5
cp %{_builddir}/amazon-ssm-agent-%{version}/extra/lockfile/LICENSE %{buildroot}/usr/share/package-licenses/amazon-ssm-agent/b7198be50f32111bf77e802f95a2dfddddb3c5a1
cp %{_builddir}/amazon-ssm-agent-%{version}/vendor/github.com/Jeffail/gabs/LICENSE %{buildroot}/usr/share/package-licenses/amazon-ssm-agent/585a86f16ab8d403801ff2c7fa494436fcd5d623
cp %{_builddir}/amazon-ssm-agent-%{version}/vendor/github.com/Microsoft/go-winio/LICENSE %{buildroot}/usr/share/package-licenses/amazon-ssm-agent/11a8fec351554e8f6c3f4dac5a1f4049dd467ba8
cp %{_builddir}/amazon-ssm-agent-%{version}/vendor/github.com/Workiva/go-datastructures/LICENSE %{buildroot}/usr/share/package-licenses/amazon-ssm-agent/1128f8f91104ba9ef98d37eea6523a888dcfa5de
cp %{_builddir}/amazon-ssm-agent-%{version}/vendor/github.com/aws/aws-sdk-go/LICENSE.txt %{buildroot}/usr/share/package-licenses/amazon-ssm-agent/2b8b815229aa8a61e483fb4ba0588b8b6c491890
cp %{_builddir}/amazon-ssm-agent-%{version}/vendor/github.com/aws/aws-sdk-go/internal/sync/singleflight/LICENSE %{buildroot}/usr/share/package-licenses/amazon-ssm-agent/d6a5f1ecaedd723c325a2063375b3517e808a2b5
cp %{_builddir}/amazon-ssm-agent-%{version}/vendor/github.com/carlescere/scheduler/LICENSE %{buildroot}/usr/share/package-licenses/amazon-ssm-agent/5a34e28e0006187ace4fa93a9ab35f1b532037a1
cp %{_builddir}/amazon-ssm-agent-%{version}/vendor/github.com/cenkalti/backoff/v4/LICENSE %{buildroot}/usr/share/package-licenses/amazon-ssm-agent/101c182fa18fd56a09164278f17e4282264c5e9e
cp %{_builddir}/amazon-ssm-agent-%{version}/vendor/github.com/cihub/seelog/LICENSE.txt %{buildroot}/usr/share/package-licenses/amazon-ssm-agent/777db49977c0fd6232b76113173a191e841ae194
cp %{_builddir}/amazon-ssm-agent-%{version}/vendor/github.com/coreos/go-semver/LICENSE %{buildroot}/usr/share/package-licenses/amazon-ssm-agent/2b8b815229aa8a61e483fb4ba0588b8b6c491890
cp %{_builddir}/amazon-ssm-agent-%{version}/vendor/github.com/creack/pty/LICENSE %{buildroot}/usr/share/package-licenses/amazon-ssm-agent/37a5e9e1835e9b179f9d7175f25c3349d47b76f8
cp %{_builddir}/amazon-ssm-agent-%{version}/vendor/github.com/davecgh/go-spew/LICENSE %{buildroot}/usr/share/package-licenses/amazon-ssm-agent/d2f340a01dd48b589a70f627cf7058c585a315e4
cp %{_builddir}/amazon-ssm-agent-%{version}/vendor/github.com/digitalocean/go-smbios/LICENSE.md %{buildroot}/usr/share/package-licenses/amazon-ssm-agent/fea2174f095f21c24ebd4c9866166ead2bbc25d0
cp %{_builddir}/amazon-ssm-agent-%{version}/vendor/github.com/emirpasic/gods/LICENSE %{buildroot}/usr/share/package-licenses/amazon-ssm-agent/4e6a5510613257c2a9e6f277abdbae52ef2ccfba
cp %{_builddir}/amazon-ssm-agent-%{version}/vendor/github.com/fsnotify/fsnotify/LICENSE %{buildroot}/usr/share/package-licenses/amazon-ssm-agent/66a9502ecba0bae239ca6ba2c3e8a2fe5558a893
cp %{_builddir}/amazon-ssm-agent-%{version}/vendor/github.com/go-git/gcfg/LICENSE %{buildroot}/usr/share/package-licenses/amazon-ssm-agent/580c0a1f1386fe13bce395d23bdaf3b14ae2e20b
cp %{_builddir}/amazon-ssm-agent-%{version}/vendor/github.com/go-git/go-billy/v5/LICENSE %{buildroot}/usr/share/package-licenses/amazon-ssm-agent/252aed5d0042e1b207cfa34525444999cdb54e3e
cp %{_builddir}/amazon-ssm-agent-%{version}/vendor/github.com/go-git/go-git/v5/LICENSE %{buildroot}/usr/share/package-licenses/amazon-ssm-agent/12652bf1fa2266f5ad64804acea3a78ab66699a2
cp %{_builddir}/amazon-ssm-agent-%{version}/vendor/github.com/golang/protobuf/LICENSE %{buildroot}/usr/share/package-licenses/amazon-ssm-agent/aa9b240f558caed367795f667629ccbca28f20b2
cp %{_builddir}/amazon-ssm-agent-%{version}/vendor/github.com/google/go-github/LICENSE %{buildroot}/usr/share/package-licenses/amazon-ssm-agent/d9eee7661376514dccfc36e54c538dd2bdcd3535
cp %{_builddir}/amazon-ssm-agent-%{version}/vendor/github.com/google/go-querystring/LICENSE %{buildroot}/usr/share/package-licenses/amazon-ssm-agent/5d833085cd09e0a70fe9071b1f2edf6d31b91d45
cp %{_builddir}/amazon-ssm-agent-%{version}/vendor/github.com/google/shlex/COPYING %{buildroot}/usr/share/package-licenses/amazon-ssm-agent/2b8b815229aa8a61e483fb4ba0588b8b6c491890
cp %{_builddir}/amazon-ssm-agent-%{version}/vendor/github.com/gorilla/websocket/LICENSE %{buildroot}/usr/share/package-licenses/amazon-ssm-agent/307711a68aa375a23d90191db6f720426cf88402
cp %{_builddir}/amazon-ssm-agent-%{version}/vendor/github.com/hectane/go-acl/LICENSE.txt %{buildroot}/usr/share/package-licenses/amazon-ssm-agent/0718575c03bdd2c991837ade51ff3c83e606b024
cp %{_builddir}/amazon-ssm-agent-%{version}/vendor/github.com/imdario/mergo/LICENSE %{buildroot}/usr/share/package-licenses/amazon-ssm-agent/eecfc0c7e0930c6ba1ed0ff2d46a0a6fa0d16d6c
cp %{_builddir}/amazon-ssm-agent-%{version}/vendor/github.com/jbenet/go-context/LICENSE %{buildroot}/usr/share/package-licenses/amazon-ssm-agent/e5e9e009a3997eb17fba187559a605766efeb0ed
cp %{_builddir}/amazon-ssm-agent-%{version}/vendor/github.com/jmespath/go-jmespath/LICENSE %{buildroot}/usr/share/package-licenses/amazon-ssm-agent/4052101a660a7d8343c13ada130123f75f1dd408
cp %{_builddir}/amazon-ssm-agent-%{version}/vendor/github.com/kevinburke/ssh_config/LICENSE %{buildroot}/usr/share/package-licenses/amazon-ssm-agent/e2790aafbdb5006d063fce3f841073b9d24ca1c7
cp %{_builddir}/amazon-ssm-agent-%{version}/vendor/github.com/mitchellh/go-homedir/LICENSE %{buildroot}/usr/share/package-licenses/amazon-ssm-agent/5ad2002bc8d2b22e2034867d159f71ba6258e18f
cp %{_builddir}/amazon-ssm-agent-%{version}/vendor/github.com/mitchellh/go-ps/LICENSE.md %{buildroot}/usr/share/package-licenses/amazon-ssm-agent/d676a57141ac47c27699fc8b03e1a2e59abb96ef
cp %{_builddir}/amazon-ssm-agent-%{version}/vendor/github.com/nightlyone/lockfile/LICENSE %{buildroot}/usr/share/package-licenses/amazon-ssm-agent/b7198be50f32111bf77e802f95a2dfddddb3c5a1
cp %{_builddir}/amazon-ssm-agent-%{version}/vendor/github.com/pmezard/go-difflib/LICENSE %{buildroot}/usr/share/package-licenses/amazon-ssm-agent/cd3e4d932cee20da681e6b3bee8139cb4f734034
cp %{_builddir}/amazon-ssm-agent-%{version}/vendor/github.com/sergi/go-diff/LICENSE %{buildroot}/usr/share/package-licenses/amazon-ssm-agent/339c6727403193323caf4e772103d3a4e8ad59db
cp %{_builddir}/amazon-ssm-agent-%{version}/vendor/github.com/stretchr/objx/LICENSE %{buildroot}/usr/share/package-licenses/amazon-ssm-agent/9d0e87d9ac5974470fc21c575854718e8b6516be
cp %{_builddir}/amazon-ssm-agent-%{version}/vendor/github.com/stretchr/testify/LICENSE %{buildroot}/usr/share/package-licenses/amazon-ssm-agent/892204393ca075d09c8b1c1d880aba1ae0a2b805
cp %{_builddir}/amazon-ssm-agent-%{version}/vendor/github.com/twinj/uuid/LICENSE %{buildroot}/usr/share/package-licenses/amazon-ssm-agent/3e8a1a16d0b1c3999be195424b7e81e6f4457b40
cp %{_builddir}/amazon-ssm-agent-%{version}/vendor/github.com/xanzy/ssh-agent/LICENSE %{buildroot}/usr/share/package-licenses/amazon-ssm-agent/669a1e53b9dd9df3474300d3d959bb85bad75945
cp %{_builddir}/amazon-ssm-agent-%{version}/vendor/github.com/xtaci/smux/LICENSE %{buildroot}/usr/share/package-licenses/amazon-ssm-agent/cb4cb443d6d45f412efe91b65e55f62bb7fb62fe
cp %{_builddir}/amazon-ssm-agent-%{version}/vendor/go.nanomsg.org/mangos/v3/LICENSE %{buildroot}/usr/share/package-licenses/amazon-ssm-agent/2b8b815229aa8a61e483fb4ba0588b8b6c491890
cp %{_builddir}/amazon-ssm-agent-%{version}/vendor/golang.org/x/crypto/LICENSE %{buildroot}/usr/share/package-licenses/amazon-ssm-agent/d6a5f1ecaedd723c325a2063375b3517e808a2b5
cp %{_builddir}/amazon-ssm-agent-%{version}/vendor/golang.org/x/net/LICENSE %{buildroot}/usr/share/package-licenses/amazon-ssm-agent/d6a5f1ecaedd723c325a2063375b3517e808a2b5
cp %{_builddir}/amazon-ssm-agent-%{version}/vendor/golang.org/x/oauth2/LICENSE %{buildroot}/usr/share/package-licenses/amazon-ssm-agent/d6a5f1ecaedd723c325a2063375b3517e808a2b5
cp %{_builddir}/amazon-ssm-agent-%{version}/vendor/golang.org/x/sync/LICENSE %{buildroot}/usr/share/package-licenses/amazon-ssm-agent/d6a5f1ecaedd723c325a2063375b3517e808a2b5
cp %{_builddir}/amazon-ssm-agent-%{version}/vendor/golang.org/x/sys/LICENSE %{buildroot}/usr/share/package-licenses/amazon-ssm-agent/d6a5f1ecaedd723c325a2063375b3517e808a2b5
cp %{_builddir}/amazon-ssm-agent-%{version}/vendor/google.golang.org/appengine/LICENSE %{buildroot}/usr/share/package-licenses/amazon-ssm-agent/2b8b815229aa8a61e483fb4ba0588b8b6c491890
cp %{_builddir}/amazon-ssm-agent-%{version}/vendor/google.golang.org/protobuf/LICENSE %{buildroot}/usr/share/package-licenses/amazon-ssm-agent/74850a25a5319bdddc0d998eb8926c18bada282b
cp %{_builddir}/amazon-ssm-agent-%{version}/vendor/gopkg.in/ini.v1/LICENSE %{buildroot}/usr/share/package-licenses/amazon-ssm-agent/e4ef54f2c30670f950d5e196afa09c88d8ef0c8a
cp %{_builddir}/amazon-ssm-agent-%{version}/vendor/gopkg.in/warnings.v0/LICENSE %{buildroot}/usr/share/package-licenses/amazon-ssm-agent/318dc4af5ea975b426db65053b4f16ca91341d15
cp %{_builddir}/amazon-ssm-agent-%{version}/vendor/gopkg.in/yaml.v2/LICENSE %{buildroot}/usr/share/package-licenses/amazon-ssm-agent/92170cdc034b2ff819323ff670d3b7266c8bffcd
cp %{_builddir}/amazon-ssm-agent-%{version}/vendor/gopkg.in/yaml.v2/LICENSE.libyaml %{buildroot}/usr/share/package-licenses/amazon-ssm-agent/ad00ce7340d89dc13ccc59920ef75cb55af5b164
cp %{_builddir}/amazon-ssm-agent-%{version}/vendor/gopkg.in/yaml.v2/NOTICE %{buildroot}/usr/share/package-licenses/amazon-ssm-agent/9522d95b2b9b284285cc3fb6ecc445aa3ee5e785
cp %{_builddir}/amazon-ssm-agent-%{version}/vendor/gopkg.in/yaml.v3/LICENSE %{buildroot}/usr/share/package-licenses/amazon-ssm-agent/b74b3b31bc15ad5e94fc1947d682aa3d84132fce
cp %{_builddir}/amazon-ssm-agent-%{version}/vendor/gopkg.in/yaml.v3/NOTICE %{buildroot}/usr/share/package-licenses/amazon-ssm-agent/9522d95b2b9b284285cc3fb6ecc445aa3ee5e785
true # nothing to do... skip this step
## install_append content
install -d -m0755 %{buildroot}/usr/bin
install -m0755 bin/linux_amd64/amazon-ssm-agent    %{buildroot}/usr/bin/amazon-ssm-agent
install -m0755 bin/linux_amd64/ssm-agent-worker    %{buildroot}/usr/bin/ssm-agent-worker
install -m0755 bin/linux_amd64/ssm-cli             %{buildroot}/usr/bin/ssm-cli
install -m0755 bin/linux_amd64/ssm-document-worker %{buildroot}/usr/bin/ssm-document-worker
install -m0755 bin/linux_amd64/ssm-session-worker  %{buildroot}/usr/bin/ssm-session-worker
install -m0755 bin/linux_amd64/ssm-session-logger  %{buildroot}/usr/bin/ssm-session-logger
mkdir -p %{buildroot}/usr/lib/systemd/system
install -m0644 packaging/linux/amazon-ssm-agent.service  %{buildroot}/usr/lib/systemd/system/
mkdir -p %{buildroot}/usr/lib/systemd/system/multi-user.target.wants
ln -s ../amazon-ssm-agent.service %{buildroot}/usr/lib/systemd/system/multi-user.target.wants/
mkdir -p %{buildroot}/usr/share/defaults/etc/amazon/ssm
install -m0644 seelog_unix.xml  %{buildroot}/usr/share/defaults/etc/amazon/ssm/seelog.xml
## install_append end

%files
%defattr(-,root,root,-)

%files autostart
%defattr(-,root,root,-)
/usr/lib/systemd/system/multi-user.target.wants/amazon-ssm-agent.service

%files bin
%defattr(-,root,root,-)
/usr/bin/amazon-ssm-agent
/usr/bin/ssm-agent-worker
/usr/bin/ssm-cli
/usr/bin/ssm-document-worker
/usr/bin/ssm-session-logger
/usr/bin/ssm-session-worker

%files data
%defattr(-,root,root,-)
/usr/share/defaults/etc/amazon/ssm/seelog.xml

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/amazon-ssm-agent/0718575c03bdd2c991837ade51ff3c83e606b024
/usr/share/package-licenses/amazon-ssm-agent/101c182fa18fd56a09164278f17e4282264c5e9e
/usr/share/package-licenses/amazon-ssm-agent/1128f8f91104ba9ef98d37eea6523a888dcfa5de
/usr/share/package-licenses/amazon-ssm-agent/11a8fec351554e8f6c3f4dac5a1f4049dd467ba8
/usr/share/package-licenses/amazon-ssm-agent/12652bf1fa2266f5ad64804acea3a78ab66699a2
/usr/share/package-licenses/amazon-ssm-agent/252aed5d0042e1b207cfa34525444999cdb54e3e
/usr/share/package-licenses/amazon-ssm-agent/2b8b815229aa8a61e483fb4ba0588b8b6c491890
/usr/share/package-licenses/amazon-ssm-agent/307711a68aa375a23d90191db6f720426cf88402
/usr/share/package-licenses/amazon-ssm-agent/318dc4af5ea975b426db65053b4f16ca91341d15
/usr/share/package-licenses/amazon-ssm-agent/339c6727403193323caf4e772103d3a4e8ad59db
/usr/share/package-licenses/amazon-ssm-agent/37a5e9e1835e9b179f9d7175f25c3349d47b76f8
/usr/share/package-licenses/amazon-ssm-agent/3e8a1a16d0b1c3999be195424b7e81e6f4457b40
/usr/share/package-licenses/amazon-ssm-agent/4052101a660a7d8343c13ada130123f75f1dd408
/usr/share/package-licenses/amazon-ssm-agent/4e6a5510613257c2a9e6f277abdbae52ef2ccfba
/usr/share/package-licenses/amazon-ssm-agent/580c0a1f1386fe13bce395d23bdaf3b14ae2e20b
/usr/share/package-licenses/amazon-ssm-agent/585a86f16ab8d403801ff2c7fa494436fcd5d623
/usr/share/package-licenses/amazon-ssm-agent/5a34e28e0006187ace4fa93a9ab35f1b532037a1
/usr/share/package-licenses/amazon-ssm-agent/5ad2002bc8d2b22e2034867d159f71ba6258e18f
/usr/share/package-licenses/amazon-ssm-agent/5d833085cd09e0a70fe9071b1f2edf6d31b91d45
/usr/share/package-licenses/amazon-ssm-agent/669a1e53b9dd9df3474300d3d959bb85bad75945
/usr/share/package-licenses/amazon-ssm-agent/66a9502ecba0bae239ca6ba2c3e8a2fe5558a893
/usr/share/package-licenses/amazon-ssm-agent/74850a25a5319bdddc0d998eb8926c18bada282b
/usr/share/package-licenses/amazon-ssm-agent/777db49977c0fd6232b76113173a191e841ae194
/usr/share/package-licenses/amazon-ssm-agent/892204393ca075d09c8b1c1d880aba1ae0a2b805
/usr/share/package-licenses/amazon-ssm-agent/92170cdc034b2ff819323ff670d3b7266c8bffcd
/usr/share/package-licenses/amazon-ssm-agent/9522d95b2b9b284285cc3fb6ecc445aa3ee5e785
/usr/share/package-licenses/amazon-ssm-agent/9d0e87d9ac5974470fc21c575854718e8b6516be
/usr/share/package-licenses/amazon-ssm-agent/aa9b240f558caed367795f667629ccbca28f20b2
/usr/share/package-licenses/amazon-ssm-agent/ad00ce7340d89dc13ccc59920ef75cb55af5b164
/usr/share/package-licenses/amazon-ssm-agent/b4f43f12b5c4f6bbaf183777fc64e38efb3e9aa5
/usr/share/package-licenses/amazon-ssm-agent/b7198be50f32111bf77e802f95a2dfddddb3c5a1
/usr/share/package-licenses/amazon-ssm-agent/b74b3b31bc15ad5e94fc1947d682aa3d84132fce
/usr/share/package-licenses/amazon-ssm-agent/cb4cb443d6d45f412efe91b65e55f62bb7fb62fe
/usr/share/package-licenses/amazon-ssm-agent/cd3e4d932cee20da681e6b3bee8139cb4f734034
/usr/share/package-licenses/amazon-ssm-agent/d2f340a01dd48b589a70f627cf7058c585a315e4
/usr/share/package-licenses/amazon-ssm-agent/d676a57141ac47c27699fc8b03e1a2e59abb96ef
/usr/share/package-licenses/amazon-ssm-agent/d6a5f1ecaedd723c325a2063375b3517e808a2b5
/usr/share/package-licenses/amazon-ssm-agent/d9eee7661376514dccfc36e54c538dd2bdcd3535
/usr/share/package-licenses/amazon-ssm-agent/e2790aafbdb5006d063fce3f841073b9d24ca1c7
/usr/share/package-licenses/amazon-ssm-agent/e4ef54f2c30670f950d5e196afa09c88d8ef0c8a
/usr/share/package-licenses/amazon-ssm-agent/e5e9e009a3997eb17fba187559a605766efeb0ed
/usr/share/package-licenses/amazon-ssm-agent/eecfc0c7e0930c6ba1ed0ff2d46a0a6fa0d16d6c
/usr/share/package-licenses/amazon-ssm-agent/fea2174f095f21c24ebd4c9866166ead2bbc25d0

%files services
%defattr(-,root,root,-)
%exclude /usr/lib/systemd/system/multi-user.target.wants/amazon-ssm-agent.service
/usr/lib/systemd/system/amazon-ssm-agent.service
