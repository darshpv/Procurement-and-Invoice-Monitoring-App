import { useState } from 'react'
import './App.css'
import TopCompaniesTable from './components/TopCompaniesTable'
import AppBar from './components/AppBar'
import CompanySummaryTable from './components/CompanySummaryTable'
import ProductSummaryTable from './components/ProductSummaryTable'
import StatusSummaryCards from './components/StatusSummary'
import DelayedDeliveriesList from './components/DelayedDeliveries'
import PendingPaymentsList from './components/PendingPayments'

function App() {

  return (
    <>
      <AppBar></AppBar>
      <StatusSummaryCards></StatusSummaryCards>
      <TopCompaniesTable></TopCompaniesTable>
      <CompanySummaryTable></CompanySummaryTable>
      <ProductSummaryTable></ProductSummaryTable>
      <DelayedDeliveriesList></DelayedDeliveriesList>
      <PendingPaymentsList></PendingPaymentsList>
    </>
  )
}

export default App
