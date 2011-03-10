# Generated from postgres-0.7.9.2008.01.28.gem by gem2rpm5 -*- rpm-spec -*-          
%define	rbname	postgres

Summary:	Ruby extension library providing an API to PostgreSQL
Name:		rubygem-%{rbname}

Version:	0.7.9.2008.01.28
Release:	3
Group:		Development/Ruby
License:	GPLv2+ or Ruby                     
URL:		http://bitbucket.org/ged/ruby-pg/
Source0:	http://rubygems.org/gems/%{rbname}-%{version}.gem
BuildRequires:	rubygems 
BuildRequires:	rubygem(rake)
%rename		ruby-%{rbname}

%description
Ruby extension library providing an API to PostgreSQL

%prep
%setup -q

%build
%gem_build

%install
rm -rf %{buildroot}
%gem_install

%clean
rm -rf %{buildroot}

%files
%dir %{ruby_gemdir}/gems/%{rbname}-%{version}
%dir %{ruby_gemdir}/gems/%{rbname}-%{version}/ext
%{ruby_gemdir}/gems/%{rbname}-%{version}/ext/*.c
%{ruby_sitearchdir}/%{rbname}.so
%{ruby_gemdir}/specifications/%{rbname}-%{version}.gemspec
