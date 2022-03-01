Summary:	An open and reliable container runtime
Name:		containerd
Version:	1.6.0
Release:	1
License:	Apache v2.0
Group:		Applications
Source0:	https://github.com/containerd/containerd/archive/v%{version}/%{name}-%{version}.tar.gz
# Source0-md5:	aa0371db45d4e149e65ccbbddcbed8b1
URL:		https://containerd.io/
BuildRequires:	btrfs-progs-devel
BuildRequires:	golang >= 1.16
BuildRequires:	rpmbuild(macros) >= 2.009
Requires:	runc
ExclusiveArch:	%go_arches
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_debugsource_packages	0

%description
containerd is an industry-standard container runtime with an emphasis
on simplicity, robustness and portability. It is available as a daemon
for Linux and Windows, which can manage the complete container
lifecycle of its host system: image transfer and storage, container
execution and supervision, low-level storage and network attachments,
etc.

%prep
%setup -q

%build
%{__make} binaries \
	GO="%__go" \
	VERSION="%{version}"

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR="$RPM_BUILD_ROOT" \
	PREFIX="%{_prefix}"

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc {ADOPTERS,BUILDING,README,RELEASES,ROADMAP,SCOPE}.md
%attr(755,root,root) %{_bindir}/containerd
%attr(755,root,root) %{_bindir}/containerd-shim
%attr(755,root,root) %{_bindir}/containerd-shim-runc-v1
%attr(755,root,root) %{_bindir}/containerd-shim-runc-v2
%attr(755,root,root) %{_bindir}/containerd-stress
%attr(755,root,root) %{_bindir}/ctr
