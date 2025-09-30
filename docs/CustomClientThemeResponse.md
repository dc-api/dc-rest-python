# CustomClientThemeResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**colors** | **List[str]** |  | 
**gradient_angle** | **int** |  | 
**base_mix** | **int** |  | 
**base_theme** | **int** |  | 

## Example

```python
from dc_rest.models.custom_client_theme_response import CustomClientThemeResponse

# TODO update the JSON string below
json = "{}"
# create an instance of CustomClientThemeResponse from a JSON string
custom_client_theme_response_instance = CustomClientThemeResponse.from_json(json)
# print the JSON string representation of the object
print(CustomClientThemeResponse.to_json())

# convert the object into a dict
custom_client_theme_response_dict = custom_client_theme_response_instance.to_dict()
# create an instance of CustomClientThemeResponse from a dict
custom_client_theme_response_from_dict = CustomClientThemeResponse.from_dict(custom_client_theme_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


