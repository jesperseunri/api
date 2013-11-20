import urllib
import requests
import base

class Sms(base.Base):

    def __init__(self):
        super(Sms, self).__init__()
        
        self.error = {}
        self.error['id'] = 'ID is invalid or undefined'
        self.error['sender'] = 'Sender value is invalid or undefined'
        self.error['address'] = 'Address value is invalid or undefined'
        self.error['msg'] = 'Message is invalid or undefined'
        self.error['url']  = 'Notify Url is not set'

        self.url = {}
        self.url['send'] = "%s/smsmessaging/%s/outbound/%s/requests?access_token=%s"
    def send(self, token = ''):
        """ Check for the required parameters """

        if not isinstance(self.address, str):
            raise Exception(self.error['address'])

        if not isinstance(self.sender, int) and not isinstance(self.sender, str):
            raise Exception(self.error['sender'])

        if not isinstance(self.msg, str):
            raise Exception(self.error['msg'])

        if not isinstance(token, str):
            raise Exception('Invalid token')

        """ Buillding parameters for the post request """

        params = {}
        params['address'] = self.address

        params['senderAddress'] = str(self.sender)
        params['message'] = urllib.quote_plus(self.msg)

        if isinstance(self.correlator, str) or isinstance(self.correlator, int):
            params['clientCorrelator'] = str(self.correlator)

        if isinstance(self.url, str):
            params['notifyURL'] = urllib.quote_plus(self.url)

        if isinstance(self.data, str):
            params['callbackData'] = self.data

        if isinstance(self.name, str):
            params['senderName'] = self.name

        url = self.url['send'] % (self.host, self.version, urllib.quote_plus(str(self.sender)), token)

        """ Set request header """

        header = {}
        header['Content-Type'] = 'application/x-www-form-urlencoded'
        header['Accept'] = 'application/json'

        return self.getResponse(url, 'post', params, header)
