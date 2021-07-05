# ========================================================================
# Description: ServiceNow Reporting
# Created by NANASAHEB YADAV
# Date : 6th July 2021
# ========================================================================

try:
    import json
    import requests
except ImportError as error:
    print("Import Error...Script stopped " + str(error))
    exit(1)


class ServiceNow:
    """
    code to get ticket dump by report id and filter data of servicenow dashboard
    """

    def _init_(self):

        try:
            self.snow_url = "url"
            self.headers = "headers"
            self.AuthenticationUsername = "users"
            self.AuthenticationPassword = "pass"
        except Exception as err:
            print(err.__str__())

    def fetch_task_data_daily(self, date):
        """
        FETCH THE DATA OF REQUESTS FOR QUEUE AND RETURN AS  JSON DATA.
        active=true
        :return:
        """
        try:
            today = date
            url = self.snow_url + "now/table/sc_task?sysparm_query=sys_created_on>{} " \
                                  "00:00:00&".format(today)

            response = requests.get(url, auth=(self.AuthenticationUsername, self.AuthenticationPassword),
                                    headers=self.headers, timeout=1000)
            # print(response.status_code)
            if response.status_code != 200:
                print(response.json())
            json_data = (response.json())
            return json_data
        except Exception as e:
            print("Error:", e.__str__())

    def download_month_requests_data(self, filename):
        """
        Download all requests data for given report id
        :return:
        """
        try:
            reportid = "cc5396361bb0741234567c4e8b4bcb55"
            url = 'https://xxxx.com/sys_report_template.do?CSV&jvar_report_id' \
                  '={}'.format(reportid)

            response = requests.get(url, auth=(self.AuthenticationUsername, self.AuthenticationPassword),
                                    headers=self.headers, timeout=1900)

            if response.status_code is not 200:
                print("Error", response.json())

            with open(filename, 'wb') as out_file:
                out_file.write(response.content)

        except Exception as err:
            print("Exception: ", err.__str__())


if __name__ == '_main_':
    obj = ServiceNow()
    obj.download_month_requests_data("UAT.csv")

    """
    #pass no of days u want to fetch data in timedelta
    date = datetime.date.today() - datetime.timedelta(days=13)
    d= "2020-08-04"
    json_data = obj.fetch_task_data_daily(d)

    sys.exit()"""
