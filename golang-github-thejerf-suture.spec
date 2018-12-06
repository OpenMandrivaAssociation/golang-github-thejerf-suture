Name:           golang-github-thejerf-suture
Summary:        Supervisor trees for Go
Version:        3.0.0
Release:        2%{?dist}
License:        MIT

# https://github.com/thejerf/suture
%global repo    suture
%global goipath github.com/thejerf/%{repo}
%global tag     v3.0.0

%gometa

URL:            %{gourl}
Source0:        %{gourl}/archive/%{tag}/%{repo}-%{version}.tar.gz

%description
%{summary}


%package        devel
Summary:        %{summary}
BuildArch:      noarch

%description    devel
%{summary}

This package contains library source intended for
building other packages which use import path with
%{goipath} prefix.


%prep
%forgeautosetup -p1


%install
%goinstall


%check
%gochecks


%files devel -f devel.file-list
%license LICENSE
%doc README.md


%changelog
* Wed Oct 24 2018 Fabio Valentini <decathorpe@gmail.com> - 3.0.0-2
- Use standard GitHub SourceURL again for consistency between releases.
- Use forgeautosetup instead of gosetup.

* Fri Sep 28 2018 Fabio Valentini <decathorpe@gmail.com> - 3.0.0-1
- Update to version 3.0.0.

* Sat Sep 15 2018 Fabio Valentini <decathorpe@gmail.com> - 2.0.3-4.20180907gitbf6ee6a
- Bump to commit bf6ee6a.

* Sun Sep 02 2018 Fabio Valentini <decathorpe@gmail.com> - 2.0.3-3.20180802git743e30e
- Bump to commit 743e30e.
- Update to use spec 3.0.

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Sun Jul 08 2018 Fabio Valentini <decathorpe@gmail.com> - 2.0.3-1
- Bump to version 2.0.3.
- Added upstream patch to prevent programs from hanging indefinitely.

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.1-5.20180103.gitbb8f537
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Tue Jan 09 2018 Fabio Valentini <decathorpe@gmail.com> - 2.0.1-4.20180103.gitbb8f537
- Bump to commit bb8f537.

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Mar  4 2017 Fabio Valentini <decathorpe@gmail.com> - 2.0.1-1
- Update to version 2.0.1.
- This includes a fix for intermittent test failures.

* Tue Feb 28 2017 Fabio Valentini <decathorpe@gmail.com> - 2.0.0-1
- First package for Fedora

