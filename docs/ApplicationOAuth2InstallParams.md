# ApplicationOAuth2InstallParams


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**scopes** | **List[str]** |  | [optional] 
**permissions** | **int** |  | [optional] 

## Example

```python
from dc_rest.models.application_o_auth2_install_params import ApplicationOAuth2InstallParams

# TODO update the JSON string below
json = "{}"
# create an instance of ApplicationOAuth2InstallParams from a JSON string
application_o_auth2_install_params_instance = ApplicationOAuth2InstallParams.from_json(json)
# print the JSON string representation of the object
print(ApplicationOAuth2InstallParams.to_json())

# convert the object into a dict
application_o_auth2_install_params_dict = application_o_auth2_install_params_instance.to_dict()
# create an instance of ApplicationOAuth2InstallParams from a dict
application_o_auth2_install_params_from_dict = ApplicationOAuth2InstallParams.from_dict(application_o_auth2_install_params_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


