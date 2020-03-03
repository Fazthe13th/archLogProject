import pandas as pd
import re
from load_data import load_data
import hashlib
import json
class parser:
    "this class will parse the log lines"
    DB_load = load_data()
    def read_file(self):
        # file = '/bracnet/arch_log/test_wireless_log.log'
        file = '/home/faz13/Downloads/wireless_log/test_head.log'
        # df = pd.read_csv(file,sep='\t', header=None, error_bad_lines=False, engine='python')
        chunksize = 100000
        j = 0
        total_line_processed = 0
        total_line_ignored = 0
        for df in pd.read_csv(file,sep='\t', header=None, error_bad_lines=False, engine='python', chunksize=chunksize, iterator=True):
            j = j + 1
            chunk_line_processed , chunk_line_ignored = self.process_chunk(df)
            total_line_processed = total_line_processed + chunk_line_processed
            total_line_ignored = total_line_ignored + chunk_line_ignored
        print("Final Chunk Count: "+ str(j))
        print("Total line processed: " + str(total_line_processed))
        print("Total line ignored: " + str(total_line_ignored))
    def process_chunk(self, chunk_df):
        "process chunks "
        chunk_line_processed = 0
        chunk_line_ignored = 0
        for index, row in chunk_df.iterrows():
            process_status = self.read_lines(row[0])
            if process_status:
                chunk_line_processed = chunk_line_processed + 1
            else:
                chunk_line_ignored = chunk_line_ignored + 1
        return chunk_line_processed,chunk_line_ignored
    def read_lines(self, line):
        "Use Regex to read the lines"
        mac_is_there = False
        plain_line = re.sub(' +', ' ', str(line))
        #regex pattern to find the necessery values
        monthday_pattern = r"^[JFMASOND][aepuco][nbrylgptvc].\d+[ ]"
        time_pattern = r"\d+[:]\d+[:]\d+"
        pop_name_pattern = r"(?<=[\d\d[:]\d\d[:]\d\d\b).+(?=(forward))"
        source_user_pattren = r"(?<=(in:)).+(?=(proto))"
        protocal_pattern = r"(?<=(proto\s))[0-9a-zA-Z_]+\s.+?(?<=([)]))"
        ip_pattern = r"\d+\.\d+\.\d+\.\d+[:]\d+"
        if re.search(r'\b' + 'src-mac' + r'\b',plain_line.lower(),flags=re.IGNORECASE):
            mac_is_there = True
            source_user_pattren = r"(?<=(forward: )).+(?=(, src-mac))"
            mac_pattern = r"(?<=(src-mac))\s\w\w:\w\w:\w\w:\w\w:\w\w:\w\w"
        else:
            mac_is_there = False
            source_user_pattren = r"(?<=(forward: )).+(?=(, proto))"
        # search for patten in the string
        try:
            ips = re.findall(ip_pattern,plain_line,flags=0)
            month_day = re.search(monthday_pattern, plain_line, flags=0)
            time = re.search(time_pattern, plain_line, flags=0)
            pop_name = re.search(pop_name_pattern, plain_line, flags=0)
            protocal = re.search(protocal_pattern, plain_line, flags=0)
            source_user = re.search(source_user_pattren, plain_line, flags=0)
            month_day_split = month_day.group().strip().split()
            if mac_is_there:
                mac = re.search(mac_pattern, plain_line, flags=0)
            if re.search(r'\b' + 'NAT' + r'\b',plain_line,flags=0):
                source_ip_full =  str(ips[2]).split(':')
                source_ip = source_ip_full[0]
                source_ip_port = source_ip_full[1]
                NAT_ip_full =  str(ips[3]).split(':')
                NAT_ip = NAT_ip_full[0]
                NAT_ip_port = NAT_ip_full[1]
                destination_ip_full =  str(ips[4]).split(':')
                destination_ip = destination_ip_full[0]
                destination_ip_port = destination_ip_full[1]

                 
            else:
                source_ip_full =  str(ips[0]).split(':')
                source_ip = source_ip_full[0]
                source_ip_port = source_ip_full[1]
                NAT_ip = None
                NAT_ip_port = None
                destination_ip_full =  str(ips[1]).split(':')
                destination_ip = destination_ip_full[0]
                destination_ip_port = destination_ip_full[1]
            log_to_hash = {
                "month": month_day_split[0],
                "day": month_day_split[1],
                "time": time.group().strip(),
                "pop_name": pop_name.group().strip(),
                "source": source_user.group().strip(),
                "mac": mac.group().strip() if mac_is_there else None,
                "protocal": protocal.group().strip(),
                "source_ip": source_ip,
                "source_ip_port": source_ip_port,
                "NAT_ip": NAT_ip,
                "NAT_ip_port": NAT_ip_port,
                "destination_ip": destination_ip,
                "destination_ip_port": destination_ip_port
            }
            log_to_hash = json.dumps(log_to_hash, sort_keys = True).encode("utf-8")
            genetrate_id = hashlib.md5(log_to_hash).hexdigest()
            log = {
                
                "month": month_day_split[0],
                "day": month_day_split[1],
                "time": time.group().strip(),
                "pop_name": pop_name.group().strip(),
                "source": source_user.group().strip(),
                "mac": mac.group().strip() if mac_is_there else None,
                "protocal": protocal.group().strip(),
                "source_ip": source_ip,
                "source_ip_port": source_ip_port,
                "NAT_ip": NAT_ip,
                "NAT_ip_port": NAT_ip_port,
                "destination_ip": destination_ip,
                "destination_ip_port": destination_ip_port
            }
            try:
                self.DB_load.load_to_database(log)
                return True
            except Exception as e:
                print("Error happed: "+ str(e))
        except Exception as e:
            if re.search(r'\b' + 'packets' + r'\b',plain_line,flags=re.IGNORECASE):
                print("This line was ignored. This exception was raised: " + str(e))
                return False

            
        
        