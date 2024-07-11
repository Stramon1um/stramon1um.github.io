from segno import helpers
import segno

#QR url
qr = segno.make('https://www.mauromaver.eu/posts/posts_omnia/omnia_focus_III/')


#qr.save('mauro.png', scale=2, dark='black', data_dark='#198259',data_light='white', quiet_zone="#198259")

#qr2.save('mauro_semplice.png', scale=4, dark='black', data_dark='#198259',data_light='white', quiet_zone="#198259")

#qr3.save('mauro_semplice.svg', scale=4, dark='black', data_dark='#198259',data_light='white', quiet_zone="#198259")

qr.save('mauro_url.png', scale=3, dark='teal', data_dark='teal',data_light='white', border=0)

qr.save('mauro_url.svg', scale=3, dark='teal', data_dark='black',data_light='white', border=0)

