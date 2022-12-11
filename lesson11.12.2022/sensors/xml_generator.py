from user_interface import temperature_view
from user_interface import wind_speed_view
from user_interface import pressure_view


def create(device=1):
    style = 'style = "font-size:30px;"'
    xml = '<xml>\n <head></head>\n <body>\n'
    xml += '     <p {}>Temperature: {} c</p>\n'\
        .format(style, temperature_view(device))
    xml += '     <p {}>Pressure: {} mmHg</p>\n'\
        .format(style, pressure_view(device))
    xml += '     <p {}>Wind Speed: {} m/s</p>\n'\
        .format(style, wind_speed_view(device))
    xml += '   </body>\n </xml>'

    with open('index.xml', 'w') as page:
        page.write(xml)

    return xml

def new_create(data,device=1):
    t,p,w = data
    style = 'style = "font-size:30px;"'
    xml = '<xml>\n <head></head>\n <body>\n'
    xml += '     <p >Temperature: {} c</p>\n'\
        .format(t)
    xml += '     <p >Pressure: {} mmHg</p>\n'\
        .format(p)
    xml += '     <p >Wind Speed: {} m/s</p>\n'\
        .format(w)
    xml += '   </body>\n </xml>'

    with open('new_index.xml', 'w') as page:
        page.write(xml)

    return data
