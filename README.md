### PublicIPChecker  
  
I wrote this to run on my server in order to keep an eye on my public IP as it sometimes will change and when it does my services go down. This grabs the current dns configured ip address of my domain name and compares that to my current public ip address. If they are different than my public IP has changed and it sends me a message alert in a predesignated teams channel using a webhook.  
  
If installing for yourself, the configs file requires yourteams webhook url.  
  
I set this script up as a cronjob but could be made into a system service as well. 