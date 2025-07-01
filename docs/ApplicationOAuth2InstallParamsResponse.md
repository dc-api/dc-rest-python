# ApplicationOAuth2InstallParamsResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**scopes** | **List[str]** |  | 
**permissions** | **str** |  | 

## Example

```python
from dc_rest.models.application_o_auth2_install_params_response import ApplicationOAuth2InstallParamsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ApplicationOAuth2InstallParamsResponse from a JSON string
application_o_auth2_install_params_response_instance = ApplicationOAuth2InstallParamsResponse.from_json(json)
# print the JSON string representation of the object
print(ApplicationOAuth2InstallParamsResponse.to_json())

# convert the object into a dict
application_o_auth2_install_params_response_dict = application_o_auth2_install_params_response_instance.to_dict()
# create an instance of ApplicationOAuth2InstallParamsResponse from a dict
application_o_auth2_install_params_response_from_dict = ApplicationOAuth2InstallParamsResponse.from_dict(application_o_auth2_install_params_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


