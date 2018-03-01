import unittest
import json
from init import app
import threading

class WebServerTestCase(unittest.TestCase):

    # initialize server class and set the expected input data
    def setUp(self):
        self.server = app.test_client()
        self.testInput  = dict(bagOfText="This is an example of text")

    def tearDown(self):
        pass

    # send a post request without the requested key (bagOfText)
    def test_invalid_request(self):
        # empty input
        response = self.server.post('/processText', content_type='form-data', data=dict())
        jsonResponse = json.loads(response.data.decode('utf-8'))
        self.assertEqual(response.status_code, 406)
        self.assertEqual(jsonResponse['errorMsg'], "Invalid Format")
        self.assertEqual(jsonResponse['wordCounter'], 0)

    # send a post with empty input
    def test_empty_request(self):
        response = self.server.post('/processText', content_type='multipart/form-data', data=dict(bagOfText=""))
        jsonResponse = json.loads(response.data.decode('utf-8'))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(jsonResponse['errorMsg'], "Input text is required!")
        self.assertEqual(jsonResponse['wordCounter'], 0)


    # send a post request with complete content
    def test_complete_post(self):
        response = self.server.post('/processText', content_type='multipart/form-data', data=dict(bagOfText="This is an example of text"))
        jsonResponse = json.loads(response.data.decode('utf-8'))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(jsonResponse['errorMsg'], "")
        self.assertEqual(jsonResponse['wordCounter'], 6)

    # multi-thread post requests
    def test_multiple_requests(self):
        requestThreads   = []
        numberOfRequests = 500
        allDone          = False

        # send a complete post request for each thread
        def request_complete_post():
            response = self.server.post('/processText', content_type='multipart/form-data', data=dict(bagOfText="This is an example of text"))
            jsonResponse = json.loads(response.data.decode('utf-8'))

            self.assertEqual(response.status_code, 200)
            self.assertEqual(jsonResponse['errorMsg'], "")
            self.assertEqual(jsonResponse['wordCounter'], 6)

        # create separated threads to send requests
        for i in range(0, numberOfRequests):
            thread = threading.Thread(target=request_complete_post)
            requestThreads.append(thread)
            thread.start()

        # wait until all threads completed the task
        while not allDone:
            allDone = True
            for t in requestThreads:
                if t.is_alive():
                    allDone = False

if __name__ == '__main__':
    unittest.main()



