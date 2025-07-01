# GithubComment


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | 
**html_url** | **str** |  | 
**user** | [**GithubUser**](GithubUser.md) |  | 
**commit_id** | **str** |  | [optional] 
**body** | **str** |  | 

## Example

```python
from dc_rest.models.github_comment import GithubComment

# TODO update the JSON string below
json = "{}"
# create an instance of GithubComment from a JSON string
github_comment_instance = GithubComment.from_json(json)
# print the JSON string representation of the object
print(GithubComment.to_json())

# convert the object into a dict
github_comment_dict = github_comment_instance.to_dict()
# create an instance of GithubComment from a dict
github_comment_from_dict = GithubComment.from_dict(github_comment_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


