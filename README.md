# ci-sandbox

The sandbox repository for Build Doctor.

This repository exists to fail on purpose. Its workflow runs a test suite that imports a module that is not in the repository, so every run of the workflow is a red build with a real log, a real job and a real commit.

Build Doctor reads that failure, works out what broke, reproduces it, proposes a fix, proves the fix by running the suite again and opens a draft pull request with the diagnosis, the patch and the evidence.

It is a test fixture, not a project. It is not part of the Build Doctor submission.
