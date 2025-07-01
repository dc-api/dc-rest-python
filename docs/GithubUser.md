# GithubUser


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | 
**login** | **str** |  | 
**html_url** | **str** |  | 
**avatar_url** | **str** |  | 

## Example

```python
from dc_rest.models.github_user import GithubUser

# TODO update the JSON string below
json = "{}"
# create an instance of GithubUser from a JSON string
github_user_instance = GithubUser.from_json(json)
# print the JSON string representation of the object
print(GithubUser.to_json())

# convert the object into a dict
github_user_dict = github_user_instance.to_dict()
# create an instance of GithubUser from a dict
github_user_from_dict = GithubUser.from_dict(github_user_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


