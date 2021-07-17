import yaml

with open('languages.yaml') as f:
    langs = yaml.load(f, Loader=yaml.FullLoader)

spec = open('rpm/hunspell-dictionaries.spec', 'w')

spec.write(r'''Summary:        Hunspell dictionaries
License:        MIT
Name:           hunspell-lang
Version:        21.07.17
Release:        1
Group:          System
Source0:        %{name}-%{version}.tar.bz2
BuildArch:      noarch

%description
Empty package - do not install

''')

head = ''
cmd = r'''
%prep
%setup -q -n %{name}-%{version}

%install

mkdir -p $RPM_BUILD_ROOT/%{_datadir}/hunspell

'''

files = '''
%files
%defattr(-,root,root,-)

'''

for k,v in langs.items():
    print('Language', k)
    head += '''
%package {lang}
Summary:        Hunspell Dictionary for {name}
License:        {license}

%description {lang}
'''.format(lang=k, name=v['name'], license=v['license']) + '%{summary}.\n\n'

    cmd += '''
cp dictionaries/dictionaries/{path}/index.aff $RPM_BUILD_ROOT/{dd}/hunspell/{lang}.aff
cp dictionaries/dictionaries/{path}/index.dic $RPM_BUILD_ROOT/{dd}/hunspell/{lang}.dic
'''.format(lang=k, path=v['path'], dd='%{_datadir}')

    files += '''
%files {lang}
%defattr(-,root,root,-)
{dd}/hunspell/{lang}.aff
{dd}/hunspell/{lang}.dic

'''.format(lang=k, dd='%{_datadir}')

spec.write(head + cmd + files)



    
