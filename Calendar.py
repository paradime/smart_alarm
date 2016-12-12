from __future__ import print_function
import httplib2
import os

from apiclient import discovery
from oauth2client import client
from oauth2client import tools
from oauth2client.file import Storage

import datetime
from datetime import timedelta

try:
    import argparse
    flags = argparse.ArgumentParser(parents=[tools.argparser]).parse_args()
except ImportError:
    flags = None

# If modifying these scopes, delete your previously saved credentials
# at ~/.credentials/calendar-python-quickstart.json
SCOPES = 'https://www.googleapis.com/auth/calendar.readonly'
CLIENT_SECRET_FILE = 'client_secret.json'
APPLICATION_NAME = 'Python Alarm App'

class Calendar:

    def get_credentials(self):
        """Gets valid user credentials from storage.

        If nothing has been stored, or if the stored credentials are invalid,
        the OAuth2 flow is completed to obtain the new credentials.

        Returns:
            Credentials, the obtained credential.
        """
        home_dir = os.path.expanduser('~')
        credential_dir = os.path.join(home_dir, '.credentials')
        if not os.path.exists(credential_dir):
            os.makedirs(credential_dir)
        credential_path = os.path.join(credential_dir,
                                    'calendar-python-quickstart.json')

        store = Storage(credential_path)
        credentials = store.get()
        if not credentials or credentials.invalid:
            flow = client.flow_from_clientsecrets(CLIENT_SECRET_FILE, SCOPES)
            flow.user_agent = APPLICATION_NAME
            if flags:
                credentials = tools.run_flow(flow, store, flags)
            else: # Needed only for compatibility with Python 2.6
                credentials = tools.run(flow, store)
            print('Storing credentials to ' + credential_path)
        return credentials

    # Gets all events for the day
    def get_events(self):
        # Uses OAuth. Retreive credentials from the API service or file system.
        credentials = self.get_credentials()

        # Init the API service. 
        http = credentials.authorize(httplib2.Http())
        service = discovery.build('calendar', 'v3', http=http)
        # Format the time correctly to retrieve all events for the current date.
        tmin = datetime.datetime.utcnow()
        now = tmin.isoformat() + 'Z' # 'Z' indicates UTC time
        tmax = datetime.datetime(year=tmin.year, month=tmin.month, day=tmin.day + 1, hour=5)
        tmax = tmax.isoformat() + 'Z' # 'Z' indicated UTC time

        # Retrieve each event from the service and add it to the results list.
        eventsResult = service.events().list(
            calendarId='primary', timeMin=now, timeMax=tmax, singleEvents=True,
            orderBy='startTime').execute()
        events = eventsResult.get('items', [])

        # If there are no events, return an empty list. If they exist, add the
        # start times and descriptions to the list
        if not events:
            return []
        event_starts = []
        for event in events: # format all events and return them
            event_starts.append(self.format_event(event))
        return event_starts

    # Accepts an event and outputs an event in the form of
    # [EVENT NAME] beginning at [TIME OF EVENT].
    def format_event(self, event):
            start_time = event['start'].get('dateTime', event['start'].get('date'))
            local_time, offset_time = start_time[:-6], start_time[-6:]
            offset_time = offset_time.replace(':', '')
            try: # Some events that are all day have problems being parsed
                event_time_formatted = datetime.datetime.strptime(local_time + offset_time, '%Y-%m-%dT%H:%M:%S%z')
            except ValueError:
                return (event['summary'] + ' all day') # Catch the all day events
            info_string = ''
            for time in event_time_formatted.strftime("%I:%M %p").split(':'):
                info_string += time.lstrip('0') + ' ' # Convert 08:00 pm to 8 pm
            return (event['summary'] + " beginning at " + info_string)
        

    # Pull all events and return a string interpretation of them
    def get_info(self):
        events = self.get_events()
        report = "Your events for today are."
        report += ". ".join(events)
        return report
