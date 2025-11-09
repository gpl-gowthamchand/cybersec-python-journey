'''
Remove Duplicate URLs
    urls = ["https://example.com", "https://test.com", "https://example.com"]
Store only unique URLs.
'''

urls = ["https://example.com", "https://test.com", "https://example.com"]

unique_urls = set(urls)
print(unique_urls)