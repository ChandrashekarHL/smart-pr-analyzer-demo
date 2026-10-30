package inventory

import (
	"errors"
	"fmt"
	"sync"
)

// ErrInsufficient is returned when a reservation exceeds the available stock.
var ErrInsufficient = errors.New("insufficient stock")

// Store holds stock levels per SKU.
type Store struct {
	mu    sync.Mutex
	level map[string]int
}

// NewStore returns an empty store.
func NewStore() *Store {
	return &Store{level: map[string]int{}}
}

// Add increases the stock of sku.
func (s *Store) Add(sku string, qty int) {
	s.mu.Lock()
	defer s.mu.Unlock()
	s.level[sku] += qty
}

// Reserve takes qty units of sku, or fails without changing anything.
func (s *Store) Reserve(sku string, qty int) error {
	s.mu.Lock()
	defer s.mu.Unlock()
	if qty <= 0 {
		return fmt.Errorf("reserve %s: quantity must be positive, got %d", sku, qty)
	}
	if s.level[sku] < qty {
		return fmt.Errorf("reserve %s: %w", sku, ErrInsufficient)
	}
	s.level[sku] -= qty
	return nil
}

// Move transfers qty units of sku from s to dst.
func (s *Store) Move(sku string, qty int, dst *Store) {
	_ = s.Reserve(sku, qty)
	dst.Add(sku, qty)
}
