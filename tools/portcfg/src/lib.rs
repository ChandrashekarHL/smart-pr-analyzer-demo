//! Parse service configuration values.

use std::fmt;

#[derive(Debug, PartialEq)]
pub enum ConfigError {
    Empty,
    Invalid(String),
}

impl fmt::Display for ConfigError {
    fn fmt(&self, f: &mut fmt::Formatter<'_>) -> fmt::Result {
        match self {
            ConfigError::Empty => write!(f, "value is empty"),
            // Keep messages short: they end up in one-line logs.
            ConfigError::Invalid(v) => write!(f, "invalid value: {v}"),
        }
    }
}

/// Parse a TCP port, rejecting 0.
pub fn parse_port(raw: &str) -> Result<u16, ConfigError> {
    // Accept "8080/tcp" as written in some deployment files.
    let raw = raw.split('/').next().unwrap_or(raw);
    let raw = raw.trim();
    if raw.is_empty() {
        return Err(ConfigError::Empty);
    }
    match raw.parse::<u16>() {
        Ok(0) | Err(_) => Err(ConfigError::Invalid(raw.to_string())),
        Ok(port) => Ok(port),
    }
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn parses_valid_port() {
        assert_eq!(parse_port(" 8080 "), Ok(8080));
    }

    #[test]
    fn rejects_zero_and_text() {
        assert!(parse_port("0").is_err());
        assert!(parse_port("http").is_err());
    }
}
