# D100 opt-in tests

`tests/**` contains opt-in fixtures and scenarios only.

## Runtime fuse

- Do not load `tests/**` during normal `START_DM.md` / bootstrap / campaign runtime.
- Test state is not current campaign state.
- Test fixture content is not D100 canon unless the same claim is independently established by an active rules/source document.
- Read a test subtree only when the user or test procedure explicitly selects that test.
