package inventory

// Levels returns a copy of the stock levels.
func (s *Store) Levels() map[string]int {
	s.mu.Lock()
	defer s.mu.Unlock()
	out := make(map[string]int, len(s.level))
	for k, v := range s.level {
		out[k] = v
	}
	return out
}
