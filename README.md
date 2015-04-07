# Python SDK for Textalytics Semantic Publishing API

> Produce more valuable content, more quickly and with lower costs, and open up new ways of doing business.


## Description
This SDK allows to use easily the functionality provided by [Textalytics Semantic Publishing API](https://textalytics.com/api-text-analysis-semantic-publishing). It has the following structure:

  * _SempubClient.py_ - main class of the client, by creating an instance, you will be able to use all the different services included in the Semantic Publishing API.
  * _config.py_ - basic configuration, including the license key that will be used to make the requests to the API.
  * _SemPubException.py_ - an exception that is thrown when the status received in the API response was not succesful. Includes Status information from the API to correct the error. 
  * _Domain.py_ - contains the classes that model the basic elements used by the services in the API.


  * _*Manager_  - contains the classes that implement the operations over the resources (manage service).
  * _extractSemanticInfo*_, _proofreadText*_ - scripts with examples on how to use the different services.

## Example usage
There are several  _examples_ with  use cases of the [Semantic Publishing](https://textalytics.com/api-text-analysis-semantic-publishing) API services. There are three services: __semantic_tagging__, to extract semantic information from a text, __check__, to proofread it, and __manage__, that allows to create and manage user-defined resources to use in the first two services.

  You can run any of them by:

1. Go to the file _config.py_ and copy your key in the **KEY** variable instead of the placeholder `<<<your license key>>>`. If you don't know what your license key is, just check your [personal area](https://textalytics.com/personal_area) at Textalytics.

2. Install dependencies. We use the [requests](http://docs.python-requests.org/) library and json module. To install requests: 

    ```pip install requests
    ```
  

3. Run any of the scripts 
    ```python [script_name]
    ```


There are currently five example scripts available:

##### _extractSemanticInfo.py_ 
Extracts semantic information using the __semantic_tagging__ service and outputs a light version of the elements detected.

##### _extractSemanticInfoWithDictionary.py_
Creates a new user-defined dictionary, adds two entities and a concept using the __manage__ service and then extracts semantic information and prints the elements detected. The text used is the same as in the script _extractSemanticInfo.py_ to better compare the advantages of defining user resources.

##### _extractSemanticInfoWithModel.py_
This script creates a new user-defined model, adds two categories using the __manage__ service, and then extracts semantic information and prints elements detected. The text used is the same as in the script _extractSemanticInfo.py_ to better compare the advantages of defining user resources.

##### _proofreadText.py_
Proofreads the given text using the __check__ service and prints the issues detected.

##### _proofreadTextWithDictionary.py
Creates a new user-defined dictionary, adds two entities and a concept using the __manage__ service, then proofreads it using the __check__ service and prints of the issues detected. 


## Contact

Do you have any questions? Do you have any suggestiongs on how we can keep improving? Have you found a bug?
Contact us at support@textalytics.com or through our [Feedback section](https://textalytics.com/core/feedback).



## Usage, license and copying

Textalytics is a cloud service provided by DAEDALUS. S.A.

This client may be used in the terms described in the LICENSE file.

For details please refer to: http://www.textalytics.com

Copyright (c) 2014, DAEDALUS S.A. All rights reserved

