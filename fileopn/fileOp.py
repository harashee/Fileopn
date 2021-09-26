
class fileOpn(object):

    @classmethod
    def extract_log(cls,log_file):

        """
        Extract the statistics of type of logs (ERROR, WARN, INFO, DEBUG) and its occurrence

        Args:
            log_file (String): Log file which is to be used to extract the statistics

        Returns:
            [Dict]: [This will have log type and its msg repetition count]
        """     
           
        with open( log_file,'r') as f:
            content = f.readlines()
        msg = {}
        for line in content:
            # line = line.replace("  "," ")
            if len(line) <= 3:
                continue
            a = line.split("  ")
            if a[1] not in msg:
                msg[a[1]] = [1, a[2]]#,' '.join(a[4:])]
            else:
                msg[a[1]][0] +=1    
        return msg
    
    def replace_string(file_path,find_str, replace_str, count = 0):
        with open( file_path,'r') as f:
            content = f.readlines()
        
        for line in content:
            if find_str in line:
                line.replace(find_str,replace_str, count)
        

        pass

    def get_string_stats():
        #TODO
        pass

    def replace_lines():
        #TODO
        pass

    def delete_lines():
        #TODO
        pass

    def search_extract_line():
        #TODO
        pass

    def count_lines():
        #TODO
        pass


if __name__ == "__main__":
    print(fileOpn.extract_log("sample_logs/test.log"))
    print(fileOpn.replace_string("sample_logs/test.log", "ERROR", "SUCESS"))