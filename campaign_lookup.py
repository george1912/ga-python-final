import requests
import json
import os
# use this
# os.path.basename(x)
#lambda
#cloudfunctions


class DevCampaignInfo:
    '''defines key info you need from a dev instance'''
    # get auth token
    url = '/rest/api/v1.3/auth/token'
    headers = {"Content-Type": "application/x-www-form-urlencoded"}
    data = {'user_name': 'XXXXXXX', 'password': 'XXXXXXXXX', 'auth_type': 'password'}
    authdata = requests.post(url, data=data, headers=headers)
    auth_dictionary=authdata.json()
    myAuthToken=auth_dictionary['authToken']
    print(myAuthToken)

    #user input
    print('Enter your campaign name:')
    user_campaign_name = input()
    url = '/rest/api/v1.3/campaigns/' + user_campaign_name 
    headers = {"Authorization": myAuthToken, "Content-Type":"application/x-www-form-urlencoded"}
    campaign = requests.get(url,  headers=headers)
    campaign_data = campaign.json()

    # search json
    linktablepathData = campaign_data['linkTablePath']
    htmlMessagePathData = campaign_data['htmlMessagePath']
    textMessagePathData = campaign_data['textMessagePath']
    seedListPathData = campaign_data['seedListPath']
    folderNameData = campaign_data['folderName']

    
    # set variables
    linktable = linktablepathData
    htmlMessagePath = htmlMessagePathData
    textMessagePath = textMessagePathData
    seedListPath = seedListPathData
    folderNamePath = folderNameData
    codex = [linktable,htmlMessagePath,textMessagePath,seedListPath,folderNamePath]


    # start getting HTML
    print('I am sending you over the HTML you asked for')
    
    url = '/rest/api/v1.3/clDocs/' + htmlMessagePath
    headers = {"Authorization": myAuthToken, "Content-Type":"application/json"}
    html_directory = requests.get(url,  headers=headers)
    html_directory_data = html_directory.json()
    # search json for HTML to export
    html_directory_html_data = html_directory_data['content']

    def lookup(self):
        print("This campaign's link table can be found here:", self.linktable)
        print("This campaign's HTML can be found here:", self.htmlMessagePath)
        print("This campaign's text file can be found here:", self.textMessagePath)
        print("This campaign's seedlist can be found here:", self.seedListPath)
        print("This campaign's folder can be found here:", self.folderNamePath)
        # print(self.html_directory_html_data)
        # print("List contains", self.codex)
        devlist = self.codex
        with open('directory_legend.txt', 'w') as filehandle:
            for listitem in devlist:
                filehandle.write('%s\n' % listitem)
        
        with open("campaign.html", "w") as file:
            file.write(self.html_directory_html_data)
        

CampaignOne = DevCampaignInfo()
CampaignOne.lookup()



