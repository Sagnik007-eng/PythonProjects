countries = ['Argentina', 'Somalia', 'Tuvalu', 'Malta', 'Armenia', 'Christmas Island', 'Uganda',
             'Central African Republic', 'Gambia', 'Morocco', 'Sint Maarten (Dutch part)', 'Tunisia', 'Aland Islands',
             'Angola', 'Yemen', 'Niue', 'Brunei Darussalam', 'Sudan', 'Holy See (Vatican City State)', 'Malaysia',
             'New Zealand', 'Palestinian Territory, Occupied', 'Iran, Islamic Republic of', 'Macedonia, Republic of',
             'Montenegro', 'Macao', 'Belarus', 'Netherlands', 'Greenland', 'Thailand', 'French Southern Territories',
             'Cyprus', "Korea, Democratic People's Republic of", 'Rwanda', 'Ethiopia', 'Saint Barthélemy', 'Botswana',
             'Puerto Rico', 'Cape Verde', 'Nicaragua', 'Croatia', 'Guadeloupe', 'Réunion', 'Belize',
             'Northern Mariana Islands', 'Indonesia', 'Serbia', 'British Indian Ocean Territory', 'Wallis and Futuna',
             'Saint Martin (French part)', 'Nigeria', 'Spain', 'Guernsey', 'Guyana', 'Namibia',
             'Venezuela, Bolivarian Republic of', 'Pitcairn', 'Suriname', 'Switzerland', 'Portugal', 'Saudi Arabia',
             'Tanzania, United Republic of', 'Norfolk Island', 'Iceland', 'Ukraine', 'Estonia', 'Nauru', 'Comoros',
             'Andorra', 'Turks and Caicos Islands', 'Guatemala', 'Cameroon', 'Chile', 'Bulgaria', 'Afghanistan',
             'Sri Lanka', 'Romania', 'Tokelau', 'Montserrat', 'Congo', 'Congo, The Democratic Republic of the',
             'Luxembourg', 'Bolivia, Plurinational State of', 'South Georgia and the South Sandwich Islands',
             'Djibouti', 'Brazil', 'Burkina Faso', 'Curaçao', 'Heard Island and McDonald Islands', 'Cook Islands',
             'Cocos (Keeling) Islands', 'China', 'Haiti', 'Swaziland', 'Mali', 'Burundi', 'Taiwan, Province of China',
             'Ireland', 'Maldives', 'France', 'Martinique', 'Nepal', 'Saint Lucia', 'Uruguay', 'Seychelles', 'Algeria',
             'Panama', 'Anguilla', 'Cuba', 'San Marino', 'Dominica', 'Germany', 'Iraq', 'Chad', 'Tonga', 'Qatar',
             'Lesotho', 'Liberia', 'Bosnia and Herzegovina', 'Canada', 'Turkey', 'French Guiana', 'Jersey', 'Niger',
             'Paraguay', 'Bangladesh', 'Barbados', 'Mauritius', 'United Kingdom', 'Bhutan', 'Isle of Man',
             'Svalbard and Jan Mayen', 'Falkland Islands (Malvinas)', "Lao People's Democratic Republic",
             'Saint Vincent and the Grenadines', 'Korea, Republic of', 'Dominican Republic', 'Philippines',
             'Austria', 'Samoa', 'South Africa', 'Australia', 'Bahamas', 'Fiji', 'Mayotte', 'Albania',
             'Sierra Leone', 'Gibraltar', 'Kazakhstan', 'French Polynesia', 'Jordan', 'Ecuador', 'Liechtenstein',
             'Solomon Islands', 'Belgium', 'Gabon', 'Bermuda', 'Georgia', 'Saint Pierre and Miquelon', 'Ghana',
             'Guinea', 'Singapore', 'Vanuatu', 'New Caledonia', 'Sao Tome and Principe', 'Mexico', 'Equatorial Guinea',
             'Pakistan', 'Marshall Islands', 'Jamaica', 'Antigua and Barbuda', 'South Sudan', 'Japan', 'Slovenia',
             'Moldova, Republic of', 'Virgin Islands, British', 'Latvia', 'Kenya', 'Trinidad and Tobago', 'Norway',
             'Timor-Leste', 'Faroe Islands', 'Zimbabwe', 'Kuwait', 'Mozambique', 'Mauritania', 'Benin', 'Togo',
             'Sweden', 'Cayman Islands', 'Mongolia', 'United States', 'United States Minor Outlying Islands',
             'Papua New Guinea', 'Hong Kong', 'Myanmar', 'Viet Nam', 'Malawi', 'Micronesia, Federated States of',
             'Aruba', 'Virgin Islands, U.S.', 'Saint Helena, Ascension and Tristan da Cunha', 'Oman',
             'Bonaire, Sint Eustatius and Saba', 'Senegal', 'Monaco', 'Russian Federation', 'Antarctica',
             'American Samoa', 'Slovakia', 'Guinea-Bissau', 'Egypt', 'Madagascar', 'Guam', 'United Arab Emirates',
             'Kiribati', 'Israel', 'Eritrea', 'Saint Kitts and Nevis', 'El Salvador', 'Lebanon', 'Poland',
             'Syrian Arab Republic', 'Cambodia', 'Czech Republic', 'Tajikistan', 'India', 'Denmark', "Côte d'Ivoire",
             'Kyrgyzstan', 'Peru', 'Italy', 'Bouvet Island', 'Palau', 'Lithuania', 'Colombia', 'Turkmenistan', 'Zambia',
             'Libya', 'Greece', 'Honduras', 'Azerbaijan', 'Costa Rica', 'Uzbekistan', 'Hungary',
             'Grenada', 'Bahrain', 'Finland']

countries.sort()

s1={len(i) for i in countries}
mx_ln=max(s1)
mn_ln=min(s1)


smallest_country_name=[i for i in countries if len(i)==mx_ln]
longest_country_name=[i for i in countries if len(i)==mn_ln]
print(smallest_country_name)
print(longest_country_name)