Summary:        Hunspell dictionaries
License:        MIT
Name:           hunspell-lang
Version:        21.07.17
Release:        1
Group:          System
Source0:        %{name}-%{version}.tar.bz2
BuildArch:      noarch

%description
Empty package - do not install


%package cs_CZ
Summary:        Hunspell Dictionary for Czech
License:        GPL-2.0

%description cs_CZ
%{summary}.


%package da_DK
Summary:        Hunspell Dictionary for Danish
License:        GPL-2.0 OR LGPL-2.1 OR MPL-1.1

%description da_DK
%{summary}.


%package de_DE
Summary:        Hunspell Dictionary for German
License:        GPL-2.0 OR GPL-3.0

%description de_DE
%{summary}.


%package en_US
Summary:        Hunspell Dictionary for English US
License:        MIT and BSD

%description en_US
%{summary}.


%package es_ES
Summary:        Hunspell Dictionary for Spanish (or Castilian)
License:        GPL-3.0 OR LGPL-3.0 OR MPL-1.1

%description es_ES
%{summary}.


%package et_ET
Summary:        Hunspell Dictionary for Estonian
License:        LGPL-2.1

%description et_ET
%{summary}.


%package fi_FI
Summary:        Hunspell Dictionary for Finnish
License:        Unknown

%description fi_FI
%{summary}.


%package fr_FR
Summary:        Hunspell Dictionary for French
License:        MPL-2.0

%description fr_FR
%{summary}.


%package hu_HU
Summary:        Hunspell Dictionary for Hungarian
License:        GPL-2.0 OR LGPL-2.1 OR MPL-1.1

%description hu_HU
%{summary}.


%package nl_NL
Summary:        Hunspell Dictionary for Dutch (or Flemish)
License:        BSD-3-Clause OR CC-BY-3.0

%description nl_NL
%{summary}.


%package ru_RU
Summary:        Hunspell Dictionary for Russian
License:        LGPL-3.0

%description ru_RU
%{summary}.


%package sv_SE
Summary:        Hunspell Dictionary for Swedish
License:        LGPL-3.0

%description sv_SE
%{summary}.


%prep
%setup -q -n %{name}-%{version}

%install

mkdir -p $RPM_BUILD_ROOT/%{_datadir}/hunspell


cp dictionaries/dictionaries/cs/index.aff $RPM_BUILD_ROOT/%{_datadir}/hunspell/cs_CZ.aff
cp dictionaries/dictionaries/cs/index.dic $RPM_BUILD_ROOT/%{_datadir}/hunspell/cs_CZ.dic

cp dictionaries/dictionaries/da/index.aff $RPM_BUILD_ROOT/%{_datadir}/hunspell/da_DK.aff
cp dictionaries/dictionaries/da/index.dic $RPM_BUILD_ROOT/%{_datadir}/hunspell/da_DK.dic

cp dictionaries/dictionaries/de/index.aff $RPM_BUILD_ROOT/%{_datadir}/hunspell/de_DE.aff
cp dictionaries/dictionaries/de/index.dic $RPM_BUILD_ROOT/%{_datadir}/hunspell/de_DE.dic

cp dictionaries/dictionaries/en/index.aff $RPM_BUILD_ROOT/%{_datadir}/hunspell/en_US.aff
cp dictionaries/dictionaries/en/index.dic $RPM_BUILD_ROOT/%{_datadir}/hunspell/en_US.dic

cp dictionaries/dictionaries/es/index.aff $RPM_BUILD_ROOT/%{_datadir}/hunspell/es_ES.aff
cp dictionaries/dictionaries/es/index.dic $RPM_BUILD_ROOT/%{_datadir}/hunspell/es_ES.dic

cp dictionaries/dictionaries/et/index.aff $RPM_BUILD_ROOT/%{_datadir}/hunspell/et_ET.aff
cp dictionaries/dictionaries/et/index.dic $RPM_BUILD_ROOT/%{_datadir}/hunspell/et_ET.dic

cp dictionaries/dictionaries/../../extras/fi/index.aff $RPM_BUILD_ROOT/%{_datadir}/hunspell/fi_FI.aff
cp dictionaries/dictionaries/../../extras/fi/index.dic $RPM_BUILD_ROOT/%{_datadir}/hunspell/fi_FI.dic

cp dictionaries/dictionaries/fr/index.aff $RPM_BUILD_ROOT/%{_datadir}/hunspell/fr_FR.aff
cp dictionaries/dictionaries/fr/index.dic $RPM_BUILD_ROOT/%{_datadir}/hunspell/fr_FR.dic

cp dictionaries/dictionaries/hu/index.aff $RPM_BUILD_ROOT/%{_datadir}/hunspell/hu_HU.aff
cp dictionaries/dictionaries/hu/index.dic $RPM_BUILD_ROOT/%{_datadir}/hunspell/hu_HU.dic

cp dictionaries/dictionaries/nl/index.aff $RPM_BUILD_ROOT/%{_datadir}/hunspell/nl_NL.aff
cp dictionaries/dictionaries/nl/index.dic $RPM_BUILD_ROOT/%{_datadir}/hunspell/nl_NL.dic

cp dictionaries/dictionaries/ru/index.aff $RPM_BUILD_ROOT/%{_datadir}/hunspell/ru_RU.aff
cp dictionaries/dictionaries/ru/index.dic $RPM_BUILD_ROOT/%{_datadir}/hunspell/ru_RU.dic

cp dictionaries/dictionaries/sv/index.aff $RPM_BUILD_ROOT/%{_datadir}/hunspell/sv_SE.aff
cp dictionaries/dictionaries/sv/index.dic $RPM_BUILD_ROOT/%{_datadir}/hunspell/sv_SE.dic

%files
%defattr(-,root,root,-)


%files cs_CZ
%defattr(-,root,root,-)
%{_datadir}/hunspell/cs_CZ.aff
%{_datadir}/hunspell/cs_CZ.dic


%files da_DK
%defattr(-,root,root,-)
%{_datadir}/hunspell/da_DK.aff
%{_datadir}/hunspell/da_DK.dic


%files de_DE
%defattr(-,root,root,-)
%{_datadir}/hunspell/de_DE.aff
%{_datadir}/hunspell/de_DE.dic


%files en_US
%defattr(-,root,root,-)
%{_datadir}/hunspell/en_US.aff
%{_datadir}/hunspell/en_US.dic


%files es_ES
%defattr(-,root,root,-)
%{_datadir}/hunspell/es_ES.aff
%{_datadir}/hunspell/es_ES.dic


%files et_ET
%defattr(-,root,root,-)
%{_datadir}/hunspell/et_ET.aff
%{_datadir}/hunspell/et_ET.dic


%files fi_FI
%defattr(-,root,root,-)
%{_datadir}/hunspell/fi_FI.aff
%{_datadir}/hunspell/fi_FI.dic


%files fr_FR
%defattr(-,root,root,-)
%{_datadir}/hunspell/fr_FR.aff
%{_datadir}/hunspell/fr_FR.dic


%files hu_HU
%defattr(-,root,root,-)
%{_datadir}/hunspell/hu_HU.aff
%{_datadir}/hunspell/hu_HU.dic


%files nl_NL
%defattr(-,root,root,-)
%{_datadir}/hunspell/nl_NL.aff
%{_datadir}/hunspell/nl_NL.dic


%files ru_RU
%defattr(-,root,root,-)
%{_datadir}/hunspell/ru_RU.aff
%{_datadir}/hunspell/ru_RU.dic


%files sv_SE
%defattr(-,root,root,-)
%{_datadir}/hunspell/sv_SE.aff
%{_datadir}/hunspell/sv_SE.dic

