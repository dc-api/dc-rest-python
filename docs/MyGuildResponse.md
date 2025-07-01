# MyGuildResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**name** | **str** |  | 
**icon** | **str** |  | [optional] 
**banner** | **str** |  | [optional] 
**owner** | **bool** |  | 
**permissions** | **str** |  | 
**features** | **List[str]** |  | 
**approximate_member_count** | **int** |  | [optional] 
**approximate_presence_count** | **int** |  | [optional] 

## Example

```python
from dc_rest.models.my_guild_response import MyGuildResponse

# TODO update the JSON string below
json = "{}"
# create an instance of MyGuildResponse from a JSON string
my_guild_response_instance = MyGuildResponse.from_json(json)
# print the JSON string representation of the object
print(MyGuildResponse.to_json())

# convert the object into a dict
my_guild_response_dict = my_guild_response_instance.to_dict()
# create an instance of MyGuildResponse from a dict
my_guild_response_from_dict = MyGuildResponse.from_dict(my_guild_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


