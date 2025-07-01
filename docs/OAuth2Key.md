# OAuth2Key


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**kty** | **str** |  | 
**use** | **str** |  | 
**kid** | **str** |  | 
**n** | **str** |  | 
**e** | **str** |  | 
**alg** | **str** |  | 

## Example

```python
from dc_rest.models.o_auth2_key import OAuth2Key

# TODO update the JSON string below
json = "{}"
# create an instance of OAuth2Key from a JSON string
o_auth2_key_instance = OAuth2Key.from_json(json)
# print the JSON string representation of the object
print(OAuth2Key.to_json())

# convert the object into a dict
o_auth2_key_dict = o_auth2_key_instance.to_dict()
# create an instance of OAuth2Key from a dict
o_auth2_key_from_dict = OAuth2Key.from_dict(o_auth2_key_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


