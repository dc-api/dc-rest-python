# CustomClientThemeShareRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**colors** | **List[str]** |  | 
**gradient_angle** | **int** |  | 
**base_mix** | **int** |  | 
**base_theme** | **int** |  | [optional] 

## Example

```python
from dc_rest.models.custom_client_theme_share_request import CustomClientThemeShareRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CustomClientThemeShareRequest from a JSON string
custom_client_theme_share_request_instance = CustomClientThemeShareRequest.from_json(json)
# print the JSON string representation of the object
print(CustomClientThemeShareRequest.to_json())

# convert the object into a dict
custom_client_theme_share_request_dict = custom_client_theme_share_request_instance.to_dict()
# create an instance of CustomClientThemeShareRequest from a dict
custom_client_theme_share_request_from_dict = CustomClientThemeShareRequest.from_dict(custom_client_theme_share_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


