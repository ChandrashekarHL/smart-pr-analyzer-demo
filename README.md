# smart-pr-analyzer-demo

A small multi-language "shop" used to demonstrate and test
[prana-reviewer](https://github.com/apps/prana-reviewer), the AI code reviewer
built in [smart-pr-analyzer](https://github.com/ChandrashekarHL/smart-pr-analyzer).

`main` is clean. Each `demo/*` branch is one pull-request scenario: either a
planted problem the reviewer should catch, or a behaviour of the GitHub App
itself. See [SCENARIOS.md](SCENARIOS.md).

| Path | Language | What it is |
|---|---|---|
| `shop/` | Python | users, orders, pricing on SQLite |
| `web/src/` | TypeScript, JavaScript | the storefront helpers |
| `services/inventory/` | Go | stock reservation |
| `tools/portcfg/` | Rust | config parsing |

```bash
python -m pytest            # Python tests
```

## Contributing

Run the tests before opening a pull request, and keep prices in integer cents.
