import hypermark as h


def test_headers():
    d = h.text(
        "# Header 1\n\n## Header 2\n\n### Header 3\n\n#### Header 4\n\n##### Header 5\n\n###### Header 6"
    )
    assert (
        d.html
        == "<h1>Header 1</h1>\n<h2>Header 2</h2>\n<h3>Header 3</h3>\n<h4>Header 4</h4>\n<h5>Header 5</h5>\n<h6>Header 6</h6>\n"
    )
    assert d.hash == b"4bfb615d263dff0ac519ceda61e814a8d6485cfe8e67619058628491ccbbaff7"
    assert (
        d.text
        == "# Header 1\n\n## Header 2\n\n### Header 3\n\n#### Header 4\n\n##### Header 5\n\n###### Header 6"
    )
    assert (
        d.content
        == b"# Header 1\n\n## Header 2\n\n### Header 3\n\n#### Header 4\n\n##### Header 5\n\n###### Header 6"
    )
    assert d.links == []

