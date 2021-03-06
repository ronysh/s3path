from pathlib import PurePosixPath, PureWindowsPath

import pytest
from s3path import PureS3Path


def test_paths_of_a_different_flavour():
    with pytest.raises(TypeError, message="'<' not supported between instances of 'PureS3Path' and 'PurePosixPath'"):
        PureS3Path('/bucket/key') < PurePosixPath('/bucket/key')

    with pytest.raises(TypeError, message="'>' not supported between instances of 'PureWindowsPath' and 'PureS3Path'"):
        PureWindowsPath('/bucket/key')> PureS3Path('/bucket/key')
