Name:		python-sz-rabbit-tools
Version: 	0.1
Release: 	1%{?dist}.sz
Summary: 	Инструменты для связи с RabbitMQ
Group: 		common
License: 	commercial
URL:		http://www.fintech.ru
Source0:	%{name}.tar.gz
BuildRoot:	%(mktemp -ud %{_tmppath}/%{name}-%{version}-%{release}-XXXXXX)
Requires:	python-kerberos
Requires:	python2-pika >= 0.12.0

#%global python_sitelib %(%{__python} -c "from distutils.sysconfig import get_python_lib;")
%global python_sitelib /usr/lib/python2.7/site-packages

%description
Инструменты для связи с RabbitMQ
позволяет прослушивать, очереди RabbitMQ, отправлять сообщения в RabbitMQ

%prep

%setup -n %{name} -q

%install
mkdir -p %{buildroot}/%{python_sitelib}/python_sz_rabbit_tools/
cp -r ./lib/* %{buildroot}/%{python_sitelib}/python_sz_rabbit_tools/

#mkdir -p %{buildroot}/usr/share/python_sz_daemon/
#cp -r ./share/* %{buildroot}/usr/share/python_sz_daemon/

%clean
rm -rf %{buildroot}

%post

%files
%defattr(644,root,root,-)
%{python_sitelib}/python_sz_rabbit_tools/base_rabbit_connector.py
%{python_sitelib}/python_sz_rabbit_tools/listener.py
%{python_sitelib}/python_sz_rabbit_tools/sender.py
%{python_sitelib}/python_sz_rabbit_tools/__init__.py
%{python_sitelib}/python_sz_rabbit_tools/tools.py
#/usr/share/python_sz_daemon/example.py


%exclude %{python_sitelib}/python_sz_rabbit_tools/*.pyc
%exclude %{python_sitelib}/python_sz_rabbit_tools/*.pyo
#%exclude /usr/share/python_sz_daemon/*.pyc
#%exclude /usr/share/python_sz_daemon/*.pyo

%doc

%changelog
* Tue Jun 18 2019 Deyneko Aleksey <deyneko@fintech.ru> 0.1-0
- Первая версия
