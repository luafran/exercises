import os
from jira.client import JIRA
import getpass

os.environ['HTTPS_PROXY'] = ''
os.environ['https_proxy'] = ''

user = raw_input("Intel username: ")
passwd = getpass.getpass("Intel Password: ")

jira = JIRA(options={'server': 'https://tracker.cba.intel.com', 'rest_api_version': '2.0.alpha1'}, basic_auth=(user, passwd))
#jira = JIRA(options={'server': 'http://jiratesting2.cba.intel.com:9095', 'rest_api_version': '2'}, basic_auth=(user, passwd))

issues = jira.search_issues('project = "CDF - Decision & Choices Services" AND issuetype = Bug AND status != Closed')

for i in issues:
    issue = jira.issue(i.key)
    print "Key: {}\nSummary: {}\nExposure: {}\nStatus: {}\n".format(i.key, issue.fields.summary.value, issue.fields.customfield_10065.value.raw['value'], issue.fields.status.value.name)
