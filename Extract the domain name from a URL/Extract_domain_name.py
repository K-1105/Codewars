# Write a function that when given a URL as a string, parses out just the domain name and returns it as a string. For example:
#
# * url = "http://github.com/carbonfive/raygun" -> domain name = "github"
# * url = "http://www.zombie-bites.com"         -> domain name = "zombie-bites"
# * url = "https://www.cnet.com"                -> domain name = cnet"

# import re

# def domain_name(url):
#     trimmed = re.search("((:\/\/)|(www\.))\w+", url).group()[3:]
#     if trimmed[0:4] == "www.":
#         trimmed = trimmed[4:]
#     return trimmed


def domain_name(url):
    return url.replace("http://", "").replace("https://", "").replace("www.", "").split(".")[0]



print(domain_name("http://github.com/carbonfive/raygun"))
print(domain_name("http://www.zombie-bites.com"))
print(domain_name("https://www.cnet.com"))