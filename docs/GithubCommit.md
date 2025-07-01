# GithubCommit


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**url** | **str** |  | 
**message** | **str** |  | 
**author** | [**GithubAuthor**](GithubAuthor.md) |  | 

## Example

```python
from dc_rest.models.github_commit import GithubCommit

# TODO update the JSON string below
json = "{}"
# create an instance of GithubCommit from a JSON string
github_commit_instance = GithubCommit.from_json(json)
# print the JSON string representation of the object
print(GithubCommit.to_json())

# convert the object into a dict
github_commit_dict = github_commit_instance.to_dict()
# create an instance of GithubCommit from a dict
github_commit_from_dict = GithubCommit.from_dict(github_commit_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


