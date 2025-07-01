# OAuth2GetKeys


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**keys** | [**List[OAuth2Key]**](OAuth2Key.md) |  | 

## Example

```python
from dc_rest.models.o_auth2_get_keys import OAuth2GetKeys

# TODO update the JSON string below
json = "{}"
# create an instance of OAuth2GetKeys from a JSON string
o_auth2_get_keys_instance = OAuth2GetKeys.from_json(json)
# print the JSON string representation of the object
print(OAuth2GetKeys.to_json())

# convert the object into a dict
o_auth2_get_keys_dict = o_auth2_get_keys_instance.to_dict()
# create an instance of OAuth2GetKeys from a dict
o_auth2_get_keys_from_dict = OAuth2GetKeys.from_dict(o_auth2_get_keys_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


