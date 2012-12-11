# Generated from postgres-0.8.1.gem by gem2rpm5 -*- rpm-spec -*-          
%define	rbname	postgres

Summary:	This is an old, deprecated version of the Ruby PostgreSQL driver that hasn't been maintained or supported since early 2008
Name:		rubygem-%{rbname}

Version:	0.8.1
Release:	2
Group:		Development/Ruby
License:	GPLv2+ or Ruby
URL:		https://bitbucket.org/ged/ruby-pg
Source0:	http://rubygems.org/gems/%{rbname}-%{version}.gem
BuildRequires:	rubygems 
BuildArch:	noarch
%rename     ruby-postgres

%description
This is an old, deprecated version of the Ruby PostgreSQL driver that hasn't
been maintained or supported since early 2008.
You should install/require 'pg' instead.
If you need the 'postgres' gem for legacy code that can't be converted, you
can
still install it using an explicit version, like so:
gem install postgres -v '0.7.9.2008.01.28'
gem uninstall postgres -v '>0.7.9.2008.01.28'
If you have any questions, the nice folks in the Google group can help:
http://goo.gl/OjOPP / ruby-pg@googlegroups.com

%package	doc
Summary:	Documentation for %{name}
Group:		Books/Computer books
Requires:	%{name} = %{EVRD}
BuildArch:	noarch

%description	doc
Documents, RDoc & RI documentation for %{name}.

%prep
%setup -q

%build
%gem_build

%install
%gem_install

%files
%dir %{ruby_gemdir}/gems/%{rbname}-%{version}
%dir %{ruby_gemdir}/gems/%{rbname}-%{version}/lib
%{ruby_gemdir}/gems/%{rbname}-%{version}/lib/*.rb
%{ruby_gemdir}/specifications/%{rbname}-%{version}.gemspec

%files doc
%doc %{ruby_gemdir}/gems/%{rbname}-%{version}/*.txt
%doc %{ruby_gemdir}/doc/%{rbname}-%{version}

%changelog
* Fri Sep 28 2012 Denis Silakov <uragan@localhost> 0.8.1-1
- Initial package
