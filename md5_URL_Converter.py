import re

Program_Version = "0.1"
print("Running version " + Program_Version)

# Makes a readable list of the lines in the md5 file
with open("md5.txt") as file:
    md5_list = file.readlines()
    # while (md5_list := file.readline().rstrip()):
    #     print(md5_list)
md5_list = [x.strip() for x in md5_list]


# The Converter itself
def main():
    # Removes the "md5:" from the string
    md5_del = re.sub("md5:","",md5)

    # gets the first 2 and second 2 leters of the md5_del string and puts a "/" at the end of both.
    md5_url_1 = md5_del[:2]+"/"
    md5_url_2 = md5_del[2:4]+"/"

    # A e621 url that never changes. it needs both the URL 1 & 2 and the full md5 + a contaner e.g: .mp4 .webm .png
    e621_static_URL = "https://static1.e621.net/data/"

    # Combines all of it together
    md5_url_mp4 = e621_static_URL + md5_url_1 + md5_url_2 + md5_del + ".mp4"

    # Ads the URL to a new line in the URL.txt file
    URL_Append = open("URL.txt", "a")
    URL_Append.write(md5_url_mp4 + "\n")
    URL_Append.close()

# sets the index number to 0 then prosces the md5 list one by one.
list_index = 0
while list_index < len(md5_list):
    # Gets the MD5
    md5 = md5_list[list_index]
    
    # Runs the Convert function
    main()

    # +1 to the index so it goes to the next line.
    list_index = list_index + 1
