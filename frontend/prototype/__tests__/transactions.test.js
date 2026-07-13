import { render, screen } from '@testing-library/svelte';
import Transactions from '../views/transactions.html';

describe('Transactions Component', () => {
  it('renders the transactions section heading', () => {
    render(Transactions);
    expect(screen.getByText('Transactions')).toBeInTheDocument();
  });

  it('renders table structure', () => {
    render(Transactions);
    const table = screen.getByRole('table');
    expect(table).toBeInTheDocument();
  });

  it('displays date column header', () => {
    render(Transactions);
    expect(screen.getByText('Date')).toBeInTheDocument();
  });

  it('displays account id column header', () => {
    render(Transactions);
    expect(screen.getByText('Account ID')).toBeInTheDocument();
  });

  it('displays transaction type column header', () => {
    render(Transactions);
    expect(screen.getByText('Type')).toBeInTheDocument();
  });

  it('displays amount column header', () => {
    render(Transactions);
    expect(screen.getByText('Amount')).toBeInTheDocument();
  });

  it('displays description column header', () => {
    render(Transactions);
    expect(screen.getByText('Description')).toBeInTheDocument();
  });
});