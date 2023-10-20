import os

class public_ip_checker () :
    def __init__(self) -> None:
        self.last_ip: str = self.extract_ip_from_text("./last_ip.txt")
        self.current_ip: str = self.get_pub_ip()
        self.notify = Notification()
        self.ERRORIPMSG = "public_IP_has_Changed_check_DNS_and_AA_Site"


    def get_pub_ip(self) -> str: 
        self.write_ip_file("./current_ip.txt")
        current_ip:str = self.extract_ip_from_text("./current_ip.txt")

        return current_ip


    def write_ip_file(self, ip_file:str) -> None:
        os.system(f"curl -sS -o ./{ip_file} http://ip4only.me/api/")


    def compare_ips(self) -> bool: 
        is_same_ip = True

        if self.current_ip != self.last_ip: 
            is_same_ip = False

        return is_same_ip


    def extract_ip_from_text(self, ip_file: str) -> str:
        try: 
            with open(ip_file, "r") as ip: 
                data = ip.read().split(",")[1]
        except Exception as e: 
            self.write_ip_file(ip_file)
            data = self.extract_ip_from_text(ip_file)
        
        return data
    

# TODO need a way to update the Old IP once the ip has been changed OR we need a way to check 
# DNS ip instead of old IP which would be better methodology anyway 




class Notification() : 
    def teams_message(self, message:str) -> None: 
        os.system(f"./teams_message.sh {message}")

    def email(self, message:str) -> None:
        pass


def main():
    pubip = public_ip_checker()
    if pubip.compare_ips() == False:
        print("different")
        pubip.notify.teams_message(pubip.ERRORIPMSG)


if __name__ == "__main__":
    main()