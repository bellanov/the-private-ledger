import { render, screen } from '@testing-library/svelte';
import Accounts from '../views/accounts.html';

describe('Accounts Component', () => {
  it('renders the accounts section heading', () => {
    render(Accounts);
    expect(screen.getByText('Accounts')).toBeInTheDocument();
  });

  it('renders table structure', () => {
    render(Accounts);
    const table = screen.getByRole('table');
    expect(table).toBeInTheDocument();
  });

  it('displays account id column header', () => {
    render(Accounts);
    expect(screen.getByText('Account ID')).toBeInTheDocument();
  });

  it('displays account name column header', () => {
    render(Accounts);
    expect(screen.getByText('Account Name')).toBeInTheDocument();
  });

  it('displays account type column header', () => {
    render(Accounts);
    expect(screen.getByText('Account Type')).toBeInTheDocument();
  });

  it('displays account balance column header', () => {
    render(Accounts);
    expect(screen.getByText('Balance')).toBeInTheDocument();
  });
});