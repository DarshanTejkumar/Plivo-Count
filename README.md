# Plivo-Count
A Flask based application that uses the Plivo API and does magic :)

## Make it work

This is divided into two parts - serving the XML and running the Flask app

### Serving XML using ngrok

Assuming you have ngrok in your global PATH variable, ```cd``` into ```ngrok_xml``` and run this command in your terminal ```ruby app.rb```. You now have a Ruby server running on http://localhost:4567/inbound which produces an XML. Now to put it in the interwebs, run the following command ```./ngrok http 4567```. You should see an output saying that the tunnel is active. Copy the ```Forwarding URL``` which is shown in the output appended by ```/inbound``` to the end of the URL. This becomes your answer_url. Replace this in the ```app.py``` found in the ```app``` folder and also in the application settings at ```manage.plivo.com```. Thats it.

### Running the Flask app

Just ```cd``` into ```app``` folder and run ```python app.py``` assuming you have all the dependencies installed :)
